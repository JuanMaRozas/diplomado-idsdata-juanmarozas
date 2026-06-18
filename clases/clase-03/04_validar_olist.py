"""
DPL1046 · Clase 3 · Script 4 · 04_validar_olist.py
---------------------------------------------------------------------------
Objetivo pedagógico: control de flujo y manejo robusto de errores aplicado
a la VALIDACIÓN de datos reales de Olist, con logging de nivel producción.

Continuidad: en la Clase 1 leímos las tablas e hicimos un inventario.
Hoy damos el siguiente paso del pipeline: VALIDAR cada fila antes de
seguir. El patrón es el de cualquier ETL: leer → validar → separar.

Construimos un validador de pagos: separa pagos válidos de los que tienen
problemas (montos no positivos, cuotas inválidas, tipo desconocido),
sin detener el proceso ante el primer error.

Tabla usada (data/raw/):
  - olist_order_payments_dataset.csv
Genera:
  - data/pagos_validos.csv      (filas que pasan todas las validaciones)
  - data/pagos_rechazados.csv   (filas con su motivo de rechazo)
  - clase3_pipeline.log         (registro de la corrida)
---------------------------------------------------------------------------
"""
import logging
from pathlib import Path

import pandas as pd


def raiz_repo() -> Path:
    aqui = Path(__file__).resolve()
    for carpeta in [aqui, *aqui.parents]:
        if (carpeta / ".git").exists() or (carpeta / "clases").is_dir():
            return carpeta
    return Path.cwd()


RAIZ = raiz_repo()
DATA = RAIZ / "data" / "raw"

# ── Logging: lo primero que se configura en cualquier script de producción ──
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s · %(levelname)s · %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.StreamHandler(),  # consola
        logging.FileHandler(RAIZ / "data" / "clase3_pipeline.log",
                            encoding="utf-8"),  # archivo persistente
    ],
)

# Tipos de pago válidos según el diccionario de datos de Olist
TIPOS_VALIDOS = {"credit_card", "boleto", "voucher", "debit_card"}


def clasificar_monto(valor: float) -> str:
    """Clasifica un pago por su monto (lógica de negocio con if/elif)."""
    if valor <= 0:
        return "invalido"
    elif valor < 50:
        return "bajo"
    elif valor < 500:
        return "medio"
    else:
        return "alto"


def validar_pago(fila: dict) -> tuple[bool, str]:
    """
    Valida un registro de pago. Devuelve (es_valido, motivo).
    Demuestra if/elif/else aplicado a validación de datos reales.
    """
    # Campo obligatorio: tipo de pago
    if pd.isna(fila["payment_type"]):
        return False, "tipo_nulo"

    # El tipo debe estar en el catálogo
    if fila["payment_type"] not in TIPOS_VALIDOS:
        return False, f"tipo_desconocido:{fila['payment_type']}"

    # El monto debe ser positivo
    if pd.isna(fila["payment_value"]) or fila["payment_value"] <= 0:
        return False, "monto_no_positivo"

    # Las cuotas deben ser >= 1 (0 cuotas no tiene sentido)
    if fila["payment_installments"] < 1:
        return False, "cuotas_invalidas"

    return True, "ok"


def main() -> None:
    ruta = DATA / "olist_order_payments_dataset.csv"

    # ── TRY/EXCEPT/FINALLY: lectura robusta del archivo ──
    try:
        logging.info(f"Leyendo {ruta.name}")
        payments = pd.read_csv(ruta)
        logging.info(f"{len(payments):,} pagos cargados")
    except FileNotFoundError:
        logging.error(f"No se encontró {ruta}. ¿Descargaste el dataset?")
        raise SystemExit(1)  # error fatal: no se puede continuar
    except pd.errors.ParserError as e:
        logging.error(f"CSV corrupto: {e}", exc_info=True)
        raise SystemExit(1)

    # ── FOR + CONTINUE: validar fila por fila, aislando las malas ──
    validos, rechazados = [], []

    for fila in payments.to_dict("records"):
        es_valido, motivo = validar_pago(fila)

        if not es_valido:
            rechazados.append({**fila, "motivo_rechazo": motivo})
            continue  # ← salta a la siguiente fila, NO detiene el loop

        # Enriquecer la fila válida con su clasificación de monto
        fila["categoria_monto"] = clasificar_monto(fila["payment_value"])
        validos.append(fila)

    # ── Resumen con logging ──
    total = len(payments)
    tasa_error = len(rechazados) / total * 100 if total else 0
    logging.info(f"Válidos: {len(validos):,} · "
                 f"Rechazados: {len(rechazados):,} · "
                 f"Tasa error: {tasa_error:.2f}%")

    # ── Escribir resultados (en la Clase 4 esto irá a Parquet/cloud) ──
    salida_ok = RAIZ / "data" / "pagos_validos.csv"
    salida_no = RAIZ / "data" / "pagos_rechazados.csv"

    pd.DataFrame(validos).to_csv(salida_ok, index=False)
    logging.info(f"Pagos válidos → {salida_ok.name}")

    if rechazados:
        df_rech = pd.DataFrame(rechazados)
        df_rech.to_csv(salida_no, index=False)
        logging.info(f"Pagos rechazados → {salida_no.name}")
        # Desglose por motivo (muy útil para reportar al "cliente")
        print("\nDesglose de rechazos por motivo:")
        print(df_rech["motivo_rechazo"]
              .value_counts().to_string())
    else:
        logging.info("No hubo pagos rechazados (dataset muy limpio).")

    print(f"\nRevisa el log de la corrida en: "
          f"{(RAIZ / 'data' / 'clase3_pipeline.log').name}")

    print("")
    print("Payments: Data Frame - payments.head(5)")
    print(payments.head(5))
    print("")
    print("Payments: Dict row 0 - payments.to_dict(records)[0]")
    print(payments.to_dict("records")[0])

if __name__ == "__main__":
    main()
