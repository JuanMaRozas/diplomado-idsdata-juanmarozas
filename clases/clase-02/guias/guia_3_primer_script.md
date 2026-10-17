# Guía 3 de 3 — Leer y ejecutar tu primer script

**DPL1046 · Clase 2 · Para repasar en casa.**

Un **script** es un archivo de texto con instrucciones, como una **receta**: Python la lee de **arriba hacia abajo**, línea por línea. Aquí lees y ejecutas `03a_leer_datos.py`.

---

## 1. Ábrelo

En VS Code, en el Explorador: `clases` → `clase-02` → `material` → **`03a_leer_datos.py`**.

## 2. Ejecútalo

Con el archivo abierto, haz clic en **▶** (arriba a la derecha). O en la terminal, **en la raíz del repo y con `(.venv)` activo**:

```bash
python clases/clase-02/material/03a_leer_datos.py
```

> `python` = el programa. Lo que sigue es la **ruta** del archivo que quieres ejecutar. Si dice `No such file`, estás en otra carpeta: escribe `pwd` y vuelve con `cd` a la carpeta del repo.

**Debes ver** algo así:

```
Filas en orders: 99441
Filas en reviews: 99224
```

## 3. Léelo línea por línea

```python
import pandas as pd
```
`import` trae una herramienta. `pandas` sirve para trabajar con tablas. `as pd` es un **apodo**: de ahora en adelante escribimos `pd`.

```python
RUTA = "data/raw/"
```
Una **variable** guarda un valor: `nombre = valor`. Aquí `RUTA` guarda un **texto** (entre comillas) con la carpeta donde están los datos.

```python
orders = pd.read_csv(RUTA + "olist_orders_dataset.csv")
```
- `pd.read_csv(...)` lee un archivo CSV y lo convierte en una tabla.
- `RUTA + "olist_orders_dataset.csv"` **pega** dos textos: queda `data/raw/olist_orders_dataset.csv`.
- `orders = ...` guarda la tabla en la variable `orders`.

```python
reviews = pd.read_csv(
    RUTA + "olist_order_reviews_dataset.csv")
```
Hace lo mismo con otra tabla. Está escrito en **dos líneas** porque es largo; mientras el paréntesis esté abierto, Python sigue leyendo.

```python
print("Filas en orders:", len(orders))
```
- `len(orders)` cuenta cuántas filas tiene la tabla.
- `print(...)` muestra algo en pantalla. Aquí muestra el texto y el número.

```python
print("Filas en reviews:", len(reviews))
```
Lo mismo con `reviews`.

> Todo lo que empieza con `#` es un **comentario**: Python lo ignora. Es una explicación para ti.

## 4. Vocabulario de hoy

| Palabra | Qué es |
|---|---|
| **Script** | Archivo `.py` con instrucciones, leído de arriba hacia abajo |
| **Comentario** | Línea que empieza con `#`; Python la ignora |
| **Variable** | Un nombre que guarda un valor (`RUTA = "data/raw/"`) |
| **`print`** | Muestra algo en pantalla |
| **`import`** | Trae una herramienta (por ejemplo, `pandas`) |
| **Ruta** | La "dirección" de un archivo (`data/raw/...`) |

---

## Tarea para la próxima clase (corta)

1. Antes de la clase, haz tu **rutina de inicio** (Guía 1): entra a la carpeta del repo, activa el entorno y corre `git pull`. Te aparecerá la carpeta `clases/clase-03`.
2. Ejecuta de nuevo `00_verificar_entorno.py` y `03a_leer_datos.py`. Deben seguir funcionando.
3. Cambia algo en `03a`: lee también **`olist_customers_dataset.csv`** y muestra cuántas filas tiene. **Guarda** el archivo y ejecútalo.
4. Ve pensando con quién harás el **proyecto integrador**: será en **parejas**.

**Pista para el paso 3:** copia el bloque de `orders` y cambia el nombre de la variable y del archivo.

## ¿Qué logramos en la Clase 2?

- [ ] Entorno validado: Python 3.12, `.venv`, pandas, pytest y las 9 tablas de Olist.
- [ ] Conozco mi stack: Terminal, Git, GitHub, Python, `.venv`, pip y VS Code, y cómo se conectan.
- [ ] Leí y ejecuté mi primer script, línea por línea.

**Próxima clase:** las 4 estructuras de Python (lista, tupla, set y diccionario) y el proyecto integrador.
