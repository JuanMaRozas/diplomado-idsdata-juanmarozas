# Pronóstico de Demanda — Serie de Tiempo con Olist

**Proyecto integrador de ejemplo** · DPL1046 · Diplomado en Ingeniería de Datos con Python

> Este es un proyecto de **referencia**, para que compares tu propio proyecto integrador contra un ejemplo terminado que cumple la rúbrica. No es para copiar tal cual — es para revisar qué significa "buenas prácticas" en la práctica.

## Problema de negocio

Una empresa de e-commerce necesita **pronosticar la demanda semanal** para planificar
inventario y logística. Sin pronóstico, compran de más (dinero congelado) o de menos
(ventas perdidas).

## Solución

Pipeline ETL 100% local que procesa datos reales de Olist (e-commerce brasileño, ~100K pedidos):

1. **Extrae** datos de 2 fuentes reales: CSVs de Olist + API pública de tipo de cambio (mindicador.cl)
2. **Transforma**: limpia, cruza pedidos con items, convierte BRL→CLP, agrega por semana
3. **Carga** a SQLite sin duplicar (idempotente — corre 2 veces = mismo resultado)
4. **Analiza**: detecta estacionalidad mensual y genera pronóstico con media móvil

## Cómo correrlo

```bash
# 1. Entra a la carpeta del proyecto de ejemplo (con el .venv activo)
cd clases/clase-08/material/proyecto-ejemplo

# 2. Instala las dependencias que falten
pip install -r requirements.txt

# 3. Los CSV de Olist ya están en data/raw/ del repo (config.yaml apunta ahí)

# 4. Corre el pipeline y los tests
python pipeline.py
pytest tests/ -v

# 5. Ver resultados en la carpeta salida/
```

## Estructura

```
├── pipeline.py          # punto de entrada (corre todo)
├── config.yaml          # configuración sin tocar código — ruta de datos, parámetros
├── src/
│   ├── extraer.py       # lee Olist CSVs + API tipo de cambio
│   ├── transformar.py   # limpia, agrega, estacionalidad, pronóstico
│   └── cargar.py        # guarda en SQLite (idempotente)
├── tests/
│   └── test_pipeline.py # 4 tests con pytest
└── salida/              # resultados generados (CSV + SQLite, no se suben a git)
```

## Rúbrica

| Criterio | Peso | Cómo se cumple aquí |
|---|---|---|
| Funcionalidad | 35% | Corre completo con `python pipeline.py`, 2 fuentes reales (CSV + API con respaldo), resultados reproducibles |
| Calidad del código | 30% | Funciones modulares por responsabilidad, `try/except` + logging con loguru, 4 tests con pytest |
| Buenas prácticas | 15% | `config.yaml` externo con rutas relativas, `requirements.txt`, README y estructura clara, carga idempotente, `data/` y `salida/` fuera de git |
| Presentación | 20% | Problema de negocio claro, demo en vivo, resultado con valor de negocio (15 min + 5 de preguntas) |

## Siguiente paso (no incluido, para discutir en la presentación)

Este pipeline se corre manualmente con `python pipeline.py`. Un siguiente paso natural — y 100% local — sería automatizarlo con **cron** (Mac/Linux) o el **Programador de tareas** (Windows) para que corra todas las semanas sin intervención. No hace falta ninguna nube para eso.
