"""
09_proteger_pii.py
==================
CLASE 4 · Lectura de Datos del Mundo Real (Bloque 2: Seguridad y privacidad)
DPL1046 · Programación en Python y Manipulación de Datos · UDLA

OBJETIVO DEL SCRIPT
-------------------
Aprender a PROTEGER datos personales (PII) antes de procesarlos o enviarlos
a la nube / a una IA externa. En Chile esto lo exige la Ley 19.628 (datos
personales). Un ingeniero de datos responsable nunca trabaja con RUTs y
correos "en crudo" si puede evitarlo.

QUÉ ES PII
----------
PII = Personally Identifiable Information = información que identifica a una
persona: RUT, nombre, email, teléfono, dirección. Hay que tratarla con cuidado.

DOS TÉCNICAS QUE MUESTRA
------------------------
    1) HASHING (seudonimizar): convertir el RUT en un código irreversible con
       hashlib. Sirve para CRUZAR datos (el mismo RUT da siempre el mismo
       código) sin guardar el RUT real.
    2) ENMASCARAR (masking): mostrar solo una parte del email (j***@gmail.com)
       para que sea legible pero no expuesto.

CÓMO SE EJECUTA
---------------
    python clases/clase-04/09_proteger_pii.py
"""

import hashlib
import logging
from pathlib import Path

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S",
)

RAIZ = Path(__file__).resolve().parents[2]
DATA_DEMO = RAIZ / "data" / "demo"
DATA_DEMO.mkdir(parents=True, exist_ok=True)

# Un "salt" es un texto secreto que se mezcla antes de hashear. Hace mucho más
# difícil que alguien adivine el RUT original probando combinaciones.
# En un proyecto real, el salt vendría del .env (¡como la clase 08!).
SALT = "udla-dpl1046-2026"


def hashear_rut(rut: str) -> str:
    """Convierte un RUT en un código irreversible y estable (seudónimo).

    El mismo RUT siempre produce el mismo hash -> sirve para cruzar tablas.
    Pero del hash NO se puede volver al RUT -> protege a la persona.
    """
    texto = (SALT + str(rut)).encode("utf-8")
    return hashlib.sha256(texto).hexdigest()[:16]   # 16 caracteres bastan


def enmascarar_email(email: str) -> str:
    """Deja visible solo la primera letra del email: j***@dominio.cl."""
    if "@" not in str(email):
        return "email_invalido"
    usuario, dominio = email.split("@", 1)
    if not usuario:
        return f"***@{dominio}"
    return f"{usuario[0]}***@{dominio}"


def main() -> None:
    logging.info("CLASE 4 · Protegiendo datos personales antes de procesarlos")

    # Datos de ejemplo que simulan una tabla de clientes con PII real.
    clientes = pd.DataFrame(
        {
            "cliente_id": [1, 2, 3],
            "rut": ["12.345.678-9", "9.876.543-2", "12.345.678-9"],  # ojo: 1 y 3 iguales
            "email": ["juan@gmail.com", "maria@udla.cl", "juan@gmail.com"],
            "compra": [50000, 32000, 18000],
        }
    )

    logging.info("ANTES (datos sensibles expuestos):")
    print(clientes.to_string(index=False))

    # --- Aplicamos las protecciones columna por columna con .apply() ---
    anonimo = clientes.copy()
    anonimo["rut_hash"] = clientes["rut"].apply(hashear_rut)
    anonimo["email_masked"] = clientes["email"].apply(enmascarar_email)

    # Quitamos las columnas crudas: ya no deben viajar en el pipeline.
    anonimo = anonimo.drop(columns=["rut", "email"])

    logging.info("DESPUÉS (PII seudonimizada / enmascarada):")
    print(anonimo.to_string(index=False))

    # Comprobamos la propiedad clave: mismo RUT -> mismo hash (filas 1 y 3).
    iguales = anonimo.loc[0, "rut_hash"] == anonimo.loc[2, "rut_hash"]
    logging.info("¿El mismo RUT produjo el mismo código? %s "
                 "(por eso aún podemos cruzar datos sin exponer el RUT).",
                 "SÍ" if iguales else "NO")

    salida = DATA_DEMO / "clientes_anonimizados.csv"
    anonimo.to_csv(salida, index=False)
    logging.info("Guardado seguro en %s. Este SÍ se puede subir a la nube.",
                 salida.name)


if __name__ == "__main__":
    main()
