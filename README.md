# Diplomado en Ingeniería de Datos con Python

**DPL1046 · Programación en Python y Manipulación de Datos**
Facultad de Ingeniería y Negocios · Instituto de Matemática, Física y Estadística · UDLA
Docente: PhD. Juan Manuel Rozas

Aquí está todo el material del curso: por cada clase, la **presentación**, las **instrucciones** y los **scripts** que ejecutamos en vivo. El curso es **100% local**: todo corre en tu propio computador, sin cuentas ni servicios en la nube.

---

## Empieza aquí

1. **Clase 1** → abre [`clases/clase-01/README.md`](clases/clase-01/README.md). Ahí está el paso a paso para armar tu entorno (Mac y Windows).
2. **Cada clase** → entra a su carpeta y sigue este orden: `README.md` (qué hacer) → `teoria.html` (presentación) → `material/` (scripts).
3. **Antes de cada clase** → actualiza tu copia con `git pull` (ver abajo).

---

## Programa del curso

9 sesiones · 3 horas por sesión (teoría y práctica en la misma clase) · modalidad online sincrónica. La sesión 9 es la presentación de los proyectos. Cada clase aparece aquí a medida que se publica su material.

### Unidad 1 — Fundamentos de Programación en Python para el Trabajo con Datos
| Clase | Sesión | Material |
|---|---|---|
| 1 | Python en la Industria Real: por qué domina el dato | [clase-01](clases/clase-01/) |
| 2 | Entorno listo y primeros pasos en Python | [clase-02](clases/clase-02/) |
| 3 | Las 4 estructuras de Python y tu proyecto integrador | *próximamente* |

### Unidad 2 — Manipulación y Transformación de Datos con Python
| Clase | Sesión | Material |
|---|---|---|
| 4 | Leer datos del mundo real: archivos y APIs | *próximamente* |
| 5 | Pandas desde cero: secretos, datos personales, filtrar y limpiar | *próximamente* |
| 6 | Resumir, combinar y guardar: groupby, merge y SQLite | *próximamente* |

### Unidad 3 — Integración de Datos y Automatización con Python
| Clase | Sesión | Material |
|---|---|---|
| 7 | Del script al programa: funciones, errores, logging, tests y un proyecto de ejemplo | *próximamente* |
| 8 | APIs avanzadas, IA local y taller de proyecto | *próximamente* |
| 9 | Presentaciones del Proyecto Integrador | *próximamente* |

---

## Actualizar tu copia del curso

Los materiales se van completando durante el curso. Antes de cada clase, desde la terminal (Terminal en Mac, **Git Bash** en Windows):

```bash
cd ~/diplomado-idsdata-juanmarozas     # la carpeta del curso
git pull                               # trae el material nuevo
source .venv/bin/activate              # Windows (Git Bash): source .venv/Scripts/activate
```

Si `git pull` da un error, no te preocupes: está resuelto paso a paso en [`clases/clase-01/guias/guia_3_actualizar_el_material.md`](clases/clase-01/guias/guia_3_actualizar_el_material.md).

> **Regla simple para no tener conflictos:** no edites los archivos del curso. Si quieres experimentar, **copia** el script a una carpeta llamada `mis_trabajos/` (Git la ignora) y modifícalo ahí.

## Primera vez (instalar todo)

Sigue [`clases/clase-01/README.md`](clases/clase-01/README.md). Resumen de lo que se instala: Git, Python 3.12, VS Code, y luego el entorno virtual del curso (`.venv`) con sus librerías.

---

## Dataset del curso

Trabajamos con **Olist Brazilian E-Commerce** (Kaggle), un dataset relacional de ~100.000 órdenes en 9 tablas. Se entrega comprimido en Blackboard (`olist_raw.zip`). Los datos **no** viven en este repositorio.

## Proyecto integrador

Es el 100% del examen. Se desarrolla en **parejas** y se presenta en la Clase 9. Cada pareja elige uno de **10 temas** sobre el dataset del curso.

➡️ **Temas, entregables y rúbrica:** [`proyecto-integrador.md`](proyecto-integrador.md)

---

## Estructura del repositorio

```
diplomado-idsdata-juanmarozas/
├── README.md                   # este archivo: por dónde empezar
├── proyecto-integrador.md      # temas, entregables y rúbrica
└── clases/
    └── clase-NN/
        ├── README.md           # qué hacer en la sesión
        ├── teoria.html         # presentación de la clase (flechas ← → para navegar)
        └── material/           # scripts y requirements de la clase
```

La Clase 1 además trae `teoria_anexo_instalacion.html` (paso a paso de instalación) y la carpeta `guias/`.
