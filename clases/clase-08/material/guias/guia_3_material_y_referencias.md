# Material y Referencias de Apoyo · Clase 8

**Diplomado en Ingeniería de Datos con Python · DPL1046**

*El proyecto integrador de principio a fin*

Los enlaces de este documento fueron revisados el 28 de octubre de 2026 y estaban activos. Ninguno es obligatorio para aprobar el curso: son para quienes quieran profundizar por su cuenta. Cada recurso está etiquetado como `GRATIS`, `LIBRO` o `HERRAMIENTA`, y ordenado por el tema de clase al que corresponde.

## Clase 8 · El proyecto integrador de principio a fin

### Organizar un proyecto de datos

- **Python Packaging User Guide — src layout vs flat layout** — [packaging.python.org/…/src-layout-vs-flat-layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) `GRATIS`
  *Por qué conviene ordenar el código en carpetas. En inglés.*

- **Python.org — Tutorial oficial: módulos** — [docs.python.org/es/3/tutorial/modules.html](https://docs.python.org/es/3/tutorial/modules.html) `GRATIS`
  *Cómo dividir tu código en archivos y usar `import`, como en `src/extraer.py`. En español.*

- **The Twelve-Factor App — III. Configuración (en español)** — [12factor.net/es/config](https://12factor.net/es/config) `GRATIS`
  *Por qué los parámetros y secretos van fuera del código.*

- **PyYAML — Documentación** — [pyyaml.org/wiki/PyYAMLDocumentation](https://pyyaml.org/wiki/PyYAMLDocumentation) `GRATIS`
  *La biblioteca que lee `config.yaml` con `yaml.safe_load`. En inglés.*

### Extraer, transformar y cargar (ETL)

- **Requests — Quickstart** — [requests.readthedocs.io/en/latest/user/quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/) `GRATIS`
  *`get`, `json`, `timeout` y códigos de respuesta, como en `extraer.py`.*

- **mindicador.cl — API de indicadores económicos de Chile** — [mindicador.cl](https://mindicador.cl/) `GRATIS`
  *La API pública del dólar que usa el proyecto de ejemplo, sin clave.*

- **Python.org — Tutorial oficial: errores y excepciones** — [docs.python.org/es/3/tutorial/errors.html](https://docs.python.org/es/3/tutorial/errors.html) `GRATIS`
  *`try / except` en detalle, para el plan B de tu fuente de datos.*

- **pandas — Agrupar con groupby** — [pandas.pydata.org/docs/user_guide/groupby.html](https://pandas.pydata.org/docs/user_guide/groupby.html) `GRATIS`
  *Referencia completa de `groupby` y `agg`, usados en `transformar.py`.*

- **SQLAlchemy — Establecer la conexión (Engine)** — [docs.sqlalchemy.org/en/20/tutorial/engine.html](https://docs.sqlalchemy.org/en/20/tutorial/engine.html) `GRATIS`
  *Qué es el `engine` que usa `cargar.py`. En inglés.*

- **SQLite — Lenguaje SQL** — [sqlite.org/lang.html](https://www.sqlite.org/lang.html) `GRATIS`
  *Referencia de las consultas SQL que acepta SQLite.*

### Pruebas y registro

- **pytest — Get started** — [docs.pytest.org/en/stable/getting-started.html](https://docs.pytest.org/en/stable/getting-started.html) `GRATIS`
  *Tu primer test y cómo leer lo que muestra `pytest`.*

- **pytest — Fixtures** — [docs.pytest.org/en/stable/how-to/fixtures.html](https://docs.pytest.org/en/stable/how-to/fixtures.html) `GRATIS`
  *Cómo preparar datos de ejemplo para los tests, como `ventas_ejemplo`.*

- **Loguru — Documentación** — [loguru.readthedocs.io/en/stable](https://loguru.readthedocs.io/en/stable/) `GRATIS`
  *La biblioteca de logging más simple que usa el proyecto de ejemplo.*

- **Python.org — Logging HOWTO** — [docs.python.org/es/3/howto/logging.html](https://docs.python.org/es/3/howto/logging.html) `GRATIS`
  *El módulo `logging` estándar de Python, en español.*

### Para tu presentación

- **Knaflic, C. N. (2015). Storytelling with Data. Wiley** — [storytellingwithdata.com/books](https://www.storytellingwithdata.com/books) `LIBRO`
  *Libro de pago, en inglés. Cómo contar una historia con datos y elegir un buen gráfico.*

- **Olist — Brazilian E-Commerce Public Dataset (Kaggle)** — [kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) `HERRAMIENTA · GRATIS`
  *Para revisar las tablas antes de tu presentación.*

### Material extra de la Clase 8 (opcional)

Si quieres profundizar en **APIs por partes (paginación)** y **IA local con Ollama**, usa las guías extra de esta carpeta (`guia_extra_1` y `guia_extra_2`). Algunos enlaces útiles:

- **PokeAPI — Documentación (paginación con limit y offset)** — [pokeapi.co/docs/v2](https://pokeapi.co/docs/v2) `HERRAMIENTA · GRATIS`
  *La API que usamos para practicar la paginación.*

- **Ollama — Sitio oficial** — [ollama.com](https://ollama.com/) `HERRAMIENTA · GRATIS`
  *Descarga e instalación en Mac y Windows.*

- **Ollama — Modelo llama3.2** — [ollama.com/library/llama3.2](https://ollama.com/library/llama3.2) `HERRAMIENTA · GRATIS`
  *Descripción del modelo que usamos y sus tamaños.*

- **Anthropic — Guía de prompt engineering** — [docs.anthropic.com/…/prompt-engineering/overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) `GRATIS`
  *Técnicas para escribir buenos prompts. Sirven con cualquier modelo.*
