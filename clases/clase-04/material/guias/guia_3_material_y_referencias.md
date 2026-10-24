# Material y Referencias de Apoyo · Clase 4

**Diplomado en Ingeniería de Datos con Python · DPL1046**

*Leer archivos y APIs*

Los enlaces de este documento fueron revisados el 22 de octubre de 2026 y estaban activos. Ninguno es obligatorio para aprobar el curso: son para quienes quieran profundizar por su cuenta. Cada recurso está etiquetado como `GRATIS`, `LIBRO` o `HERRAMIENTA`, y ordenado por el tema de clase al que corresponde.

## Clase 4 · Leer archivos y APIs

### Leer y guardar archivos: CSV, Excel, JSON y Parquet

- **pandas — Guía de usuario: IO tools (text, CSV, HDF5, …)** — [pandas.pydata.org/docs/user_guide/io.html](https://pandas.pydata.org/docs/user_guide/io.html) `GRATIS`
  *La referencia oficial de todos los formatos que pandas lee y escribe, en inglés. Busca el formato con Ctrl+F.*

- **pandas — read_csv, read_excel, read_parquet y json_normalize** — [read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) · [read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html) · [read_parquet](https://pandas.pydata.org/docs/reference/api/pandas.read_parquet.html) · [json_normalize](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html) `GRATIS`
  *Cada función con todos sus parámetros (usecols, nrows, sep, sheet_name…) y ejemplos al final.*

- **JSON — Introducción al formato** — [json.org/json-es.html](https://www.json.org/json-es.html) `GRATIS`
  *Explica la sintaxis de JSON en español, en una sola página.*

- **Python.org — Módulo csv de la biblioteca estándar** — [docs.python.org/es/3/library/csv.html](https://docs.python.org/es/3/library/csv.html) `GRATIS`
  *Cómo leer CSV sin pandas. Sirve para entender qué hay "debajo" de read_csv.*

- **Apache Parquet — Visión general** — [parquet.apache.org/docs/overview](https://parquet.apache.org/docs/overview/) `GRATIS`
  *Por qué Parquet guarda por columnas y comprime. En inglés.*

- **McKinney, W. — Python for Data Analysis (3ª ed.), cap. 6 «Data Loading, Storage, and File Formats»** — [wesmckinney.com/book/accessing-data](https://wesmckinney.com/book/accessing-data) `GRATIS · LIBRO`
  *Gratis en línea, en inglés. Cubre CSV, Excel, JSON y más.*

### APIs y peticiones web

- **Requests — Quickstart** — [requests.readthedocs.io/en/latest/user/quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/) `GRATIS`
  *La biblioteca que usamos en clase: get, json(), timeout, códigos de respuesta. En inglés.*

- **MDN — Códigos de estado de respuesta HTTP** — [developer.mozilla.org/es/docs/Web/HTTP/Status](https://developer.mozilla.org/es/docs/Web/HTTP/Status) `GRATIS`
  *Qué significan el 200, 404, 500 y los demás. En español.*

- **MDN — Generalidades del protocolo HTTP** — [developer.mozilla.org/es/docs/Web/HTTP/Overview](https://developer.mozilla.org/es/docs/Web/HTTP/Overview) `GRATIS`
  *La base de cómo se piden y se responden los datos en la web.*

- **PokeAPI — API pública, sin clave, para practicar** — [pokeapi.co/docs/v2](https://pokeapi.co/docs/v2) `HERRAMIENTA · GRATIS`
  *Ideal para practicar pedidos y JSON anidado sin necesitar registro.*

- **mindicador.cl — Indicadores económicos de Chile (dólar, UF, UTM)** — [mindicador.cl](https://mindicador.cl/) `HERRAMIENTA · GRATIS`
  *La API que usamos en clase. Si un día no responde, es normal: practica el try / except.*

### Tu proyecto integrador

- **Olist — Brazilian E-Commerce Public Dataset (Kaggle)** — [kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) `HERRAMIENTA · GRATIS`
  *Descripción oficial de las 9 tablas. En el curso ya lo tienes en data/raw/.*
