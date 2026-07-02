# Pronóstico de Demanda — Serie de Tiempo con Olist

**Proyecto integrador de ejemplo** · DPL1046 · Diplomado en Ingeniería de Datos con Python

## Problema de negocio

Una empresa de e-commerce necesita **pronosticar la demanda semanal** para planificar
inventario y logística. Sin pronóstico, compran de más (dinero congelado) o de menos
(ventas perdidas).

## Solución

Pipeline ETL que procesa datos reales de Olist (e-commerce brasileño, ~100K pedidos):

1. **Extrae** datos de 2 fuentes: CSVs de Olist + API de tipo de cambio (mindicador.cl)
2. **Transforma**: limpia, cruza pedidos con items, convierte BRL→CLP, agrega por semana
3. **Carga** a SQLite sin duplicar (idempotente — corre 2 veces = mismo resultado)
4. **Analiza**: detecta estacionalidad mensual y genera pronóstico con media móvil

## Cómo correrlo

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Poner los CSVs de Olist en la carpeta datos/
#    Descargar de: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

# 3. Correr el pipeline
python pipeline.py

# 4. Correr los tests
pytest tests/ -v

# 5. Ver resultados en salida/
```

## Estructura

```
├── pipeline.py          # punto de entrada (corre todo)
├── config.yaml          # configuración sin tocar código
├── src/
│   ├── extraer.py       # lee Olist CSVs + API tipo de cambio
│   ├── transformar.py   # limpia, agrega, estacionalidad, pronóstico
│   └── cargar.py        # guarda en SQLite (idempotente)
├── tests/
│   └── test_pipeline.py # 4 tests con pytest
├── datos/               # CSVs de Olist (no se suben a git)
└── salida/              # resultados generados
```

## Rúbrica

| Criterio | Cómo se cumple |
|---|---|
| Funcionalidad (35%) | Pipeline corre completo, 2 fuentes (CSV + API), resultado con valor |
| Calidad del código (30%) | Funciones modulares, logging, 4 tests con pytest |
| Buenas prácticas (15%) | config.yaml, idempotencia, datos en .gitignore |
| Presentación (20%) | Problema claro, demo en vivo, resultado con valor de negocio |
