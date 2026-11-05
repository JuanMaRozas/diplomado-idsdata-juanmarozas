# Pronóstico de Demanda — Serie de Tiempo con Olist

**Proyecto integrador de ejemplo** · DPL1046 · Diplomado en Ingeniería de Datos con Python

> Este es un proyecto de **referencia**, para que compares tu propio proyecto integrador contra un ejemplo terminado que cumple la rúbrica. No es para copiar tal cual — es para revisar qué significa "buenas prácticas" en la práctica.

## Problema de negocio

Una empresa de e-commerce necesita **pronosticar la demanda semanal** para planificar
inventario y logística. Sin pronóstico, compran de más (dinero congelado) o de menos
(ventas perdidas).

## Solución

Pipeline ETL 100% local que procesa datos reales de Olist (e-commerce brasileño, ~100K pedidos):

1. **Extrae** datos de 2 fuentes reales: CSVs de Olist + API pública de tipo de cambio (mindicador.cl, con valor de respaldo si falla)
2. **Transforma**: filtra pedidos entregados, cruza pedidos con ítems, convierte BRL→CLP, resume por semana y por mes, y pronostica
3. **Carga** a SQLite y CSV; si corres el pipeline dos veces, el resultado es el mismo (no duplica)

## Cómo correrlo

Siempre **desde la raíz del repo**, con el `.venv` activo:

```bash
# 1. Instala las librerías que falten
pip install -r clases/clase-08/material/proyecto-ejemplo/requirements.txt

# 2. Corre el pipeline (los CSV de Olist deben estar en data/raw/)
python clases/clase-08/material/proyecto-ejemplo/pipeline.py

# 3. Corre los tests
pytest clases/clase-08/material/proyecto-ejemplo/ -v

# 4. Mira los resultados en la carpeta salida/
```

## Estructura

```
├── pipeline.py        # el pipeline completo: extraer, transformar y cargar
├── test_pipeline.py   # 10 tests con pytest
├── requirements.txt   # librerías
└── README.md
```

Los resultados se guardan en `salida/` (CSV, base SQLite y el diario `pipeline.log`), que no se sube a git.

## Rúbrica

| Criterio | Peso | Cómo se cumple aquí |
|---|---|---|
| Funcionalidad | 35% | Corre completo con un solo comando, 2 fuentes reales (CSV + API con respaldo), resultados reproducibles |
| Calidad del código | 30% | Una función por responsabilidad con docstring, `try/except` + `logging`, 10 tests con pytest (3 por función de transformación) |
| Buenas prácticas | 15% | Parámetros ordenados al inicio, rutas relativas, `requirements.txt`, README, carga sin duplicar, `data/` y `salida/` fuera de git |
| Presentación | 20% | Problema de negocio claro, demo en vivo, resultado con valor de negocio (15 min + 5 de preguntas) |

## Siguiente paso (no incluido, para discutir en la presentación)

Este pipeline se corre manualmente con `python pipeline.py`. Un siguiente paso natural — y 100% local — sería automatizarlo con **cron** (Mac/Linux) o el **Programador de tareas** (Windows) para que corra todas las semanas sin intervención. No hace falta ninguna nube para eso.
