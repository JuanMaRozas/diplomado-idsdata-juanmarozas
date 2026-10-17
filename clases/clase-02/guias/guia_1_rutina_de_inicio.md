# Guía 1 de 3 — Tu rutina de inicio de cada clase

**DPL1046 · Hazla al comenzar cada clase (toma 5 minutos).**

Esta es nuestra "rutina corta palos": seis pasos que repetiremos **igual en todas las clases**. Si los haces en orden, tu computador queda listo para trabajar.

> Usa **Terminal** (Mac) o **Git Bash** (Windows). **Nunca** CMD ni PowerShell.

---

## Los 6 pasos

### 1. Abre la terminal y entra a la carpeta del curso

```bash
cd ~/diplomado-idsdata-juanmarozas
pwd
```

`pwd` te muestra dónde estás. Debe terminar en `diplomado-idsdata-juanmarozas`.

> Si tu carpeta quedó en otro lugar (por ejemplo, el Escritorio), mira la **Guía 2**, problema 6.

### 2. Abre VS Code en esa carpeta

```bash
code .
```

En VS Code se abre el Explorador a la izquierda con las carpetas del curso.

### 3. Activa el entorno virtual (`.venv`)

| Sistema | Comando |
|---|---|
| **Windows (Git Bash)** | `source .venv/Scripts/activate` |
| **Mac (Terminal)** | `source .venv/bin/activate` |

Cuando funciona, aparece **`(.venv)`** al inicio de la línea de la terminal:

```
(.venv) usuario@equipo diplomado-idsdata-juanmarozas %
```

> **Importante:** VS Code a veces activa el `.venv` solo al abrir la terminal. Si **ya ves `(.venv)`, no lo actives otra vez**. (Si lo activaste dos veces y ves `((.venv) )`, es solo estético: escribe `deactivate` y actívalo una sola vez, o abre una terminal nueva).

### 4. Trae el material nuevo con `git pull`

```bash
git pull
```

`git pull` significa "tráeme lo nuevo de GitHub". Descarga solo lo que cambió y **no borra tus archivos**. Debes ver una lista con la carpeta de la clase de hoy (por ejemplo, `clases/clase-02`). Si dice `Already up to date` y ya ves la carpeta de la clase, también está bien.

### 5. Valida que todo funciona

Cada clase te indicaré un script de validación. En la Clase 2 es:

```bash
python clases/clase-02/material/00_verificar_entorno.py
```

Es un semáforo: cada línea dice **OK** o **FALTA**, y si falta algo, te dice qué hacer. Repite hasta ver **TODO LISTO**.

> Si instalas algo con `pip` y tu internet es lento, puede tardar. Es normal.

### 6. Avisa si algo no funcionó

No te quedes atrás: levanta la mano o escríbelo en el chat. Casi todos los problemas ya los hemos visto y tienen solución (mira la **Guía 2**).

---

## Checklist rápido

- [ ] Estoy dentro de la carpeta `diplomado-idsdata-juanmarozas` (`pwd`).
- [ ] VS Code está abierto en esa carpeta.
- [ ] Veo `(.venv)` en mi terminal.
- [ ] `git pull` terminó sin errores.
- [ ] El script de validación dice **TODO LISTO**.

## Si hay que recrear el entorno

Si no tienes `.venv` o moviste la carpeta y dejó de funcionar:

```bash
bash clases/clase-01/material/setup_local.sh
```

Tarda unos 7 minutos. Si se detiene sin mensaje, usa el plan B de la Guía 2, problema 2.
