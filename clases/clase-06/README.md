# Clase 6 — Automatización, Orquestación y Buenas Prácticas de Producción
**DPL1046 · Unidad 2: Manipulación y Transformación de Datos con Python**

De un script que funciona hoy a un programa que corre todas las noches sin que lo mires.

## Instalación
```bash
pip install -r requirements.txt
```
No se necesita internet: los scripts generan sus propios datos de ejemplo (`_datos_demo.py`).

## Scripts (en orden de la clase)
| Archivo | Bloque | Qué demuestra |
|---|---|---|
| `00_version_fea.py` | 1 | El "antes": script feo, todo amontonado, con print |
| `01_de_script_a_programa.py` | 1 | El "después": funciones + logging + config externa |
| `02_pipeline_robusto.py` | 2 | Reintentos (retry) + idempotencia + manejo de errores |
| `03_validacion.py` | 3 | Contrato de datos: validar calidad antes de seguir |
| `test_validacion.py` | 3 | Tests automáticos con `pytest` |
| `04_pipeline_produccion.py` | Cierre | Todo junto: el pipeline nocturno completo |

## Cómo correr
```bash
python 01_de_script_a_programa.py
python 02_pipeline_robusto.py      # córrelo dos veces: la 2da no rehace nada
python 03_validacion.py
pytest -v
python 04_pipeline_produccion.py
```
