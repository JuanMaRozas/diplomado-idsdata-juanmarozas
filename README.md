# Diplomado en Ingeniería de Datos con Python

**DPL1046 · Programación en Python y Manipulación de Datos**
Facultad de Ingeniería y Negocios · Instituto de Matemática, Física y Estadística · UDLA
Docente: PhD. Juan Manuel Rozas · Junio–Julio 2026

Repositorio de material para los alumnos del diplomado. Cada clase tiene su carpeta con los **scripts** que ejecutaremos en vivo y el **material teórico**.

> **Antes de cada clase:** `git pull` para tener la última versión del material.

---

## Cómo empezar

```bash
# 1. Clonar el repositorio (una sola vez)
git clone https://github.com/JuanMaRozas/diplomado-idsdata-juanmarozas.git
cd diplomado-idsdata-juanmarozas

# 2. Preparar el entorno (ver instrucciones de cada clase)
cd clases/clase-01/material
bash setup_local.sh
```

---

## Programa del curso

9 sesiones · 3 horas por sesión · 19:15–22:30 · Modalidad online sincrónica (ZOOM)

### Unidad 1 — Fundamentos de Programación en Python para el Trabajo con Datos
| Clase | Fecha | Sesión | Material |
|---|---|---|---|
| 1 | 09-06-2026 | Python en la Industria Real: por qué domina el dato | [clase-01](clases/clase-01/) |
| 2 | 11-06-2026 | Estructuras de Datos y Control de Flujo con Foco Industrial | *próximamente* |
| 3 | 16-06-2026 | Lectura de Datos del Mundo Real: Archivos, APIs y Fuentes Industriales | *próximamente* |

### Unidad 2 — Manipulación y Transformación de Datos con Python
| Clase | Fecha | Sesión | Material |
|---|---|---|---|
| 4 | 18-06-2026 | Pandas en Profundidad: el Motor de la Ingeniería de Datos | *próximamente* |
| 5 | 23-06-2026 | Transformaciones Avanzadas y Cloud: de Local a AWS | *próximamente* |
| 6 | 25-06-2026 | Automatización, Orquestación y Buenas Prácticas de Producción | *próximamente* |

### Unidad 3 — Integración de Datos y Automatización con Python
| Clase | Fecha | Sesión | Material |
|---|---|---|---|
| 7 | 30-06-2026 | Integración de APIs Avanzada: Ecosistema Real de la Industria | *próximamente* |
| 8 | 02-07-2026 | IA Aplicada a Datos: LLMs, Embeddings y el Futuro del Rol | *próximamente* |
| 9 | 07-07-2026 | Proyecto Integrador: Presentaciones y Cierre del Diplomado | *próximamente* |

---

## Dataset del curso

Trabajamos con **Olist Brazilian E-Commerce** (Kaggle), un dataset relacional de ~100.000 órdenes en 9 tablas. Se entrega comprimido en Blackboard; también puede descargarse con `download_olist.py` usando tu token de Kaggle. Los datos **no** viven en este repositorio.

## Proyecto integrador

Es el 100% del examen. Se desarrolla en **equipos de 4 personas** (~7 grupos) a lo largo del curso y se presenta en la Clase 9. Cada equipo elige uno de **10 temas** sobre el dataset del curso; cada unidad tiene un entregable parcial que se construye en las prácticas de clase.

➡️ **Detalle completo, temas y rúbrica:** [`proyecto-integrador.md`](proyecto-integrador.md)

## Estructura del repositorio

```
clases/clase-NN/
├── teoria.html        # presentación teórica de la clase
├── README.md          # qué hacer en la sesión
└── material/          # scripts .py y .sh para ejecutar
```
