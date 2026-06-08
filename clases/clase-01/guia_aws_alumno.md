# Guía del alumno — AWS (espejo en la nube)

En la **Clase 1, esto es solo demostrativo**: el profe lo muestra, tú miras. **No necesitas cuenta de AWS todavía.** Esta guía queda como **referencia para la Unidad 2**, cuando tu proyecto necesite subir datos a la nube. Guárdala para cuando llegue el momento.

> El curso es *local-first*: primero todo funciona en tu computador. La nube es el "espejo" que refleja ese trabajo.

---

## ¿Qué es lo que viste en la demo?

- **S3** = el almacenamiento de archivos de Amazon. Un "disco duro infinito" en internet, donde en la industria vive el dato.
- **Bucket** = la carpeta raíz dentro de S3. Su nombre es único en todo el mundo.
- **Zona `raw/`** = donde dejamos los datos crudos, tal como llegan. Después vienen zonas "limpias".
- **La arquitectura del curso:** `S3 (raw) → Glue (transformar) → Athena (consultar con SQL) → QuickSight (visualizar)`.

---

## Cuando llegues a la Unidad 2: cómo hacerlo tú

### 1. Crea tu cuenta AWS
- Entra a **https://aws.amazon.com** → **Create an AWS Account**.
- Usa el **Free Tier** (capa gratuita): alcanza de sobra para el curso.
- Pedirá tarjeta para verificación, pero lo que haremos no genera costos relevantes.

### 2. Crea tus credenciales (Access Keys)
- En la consola AWS → **IAM → Users → tu usuario → Security credentials → Create access key**.
- Guarda el **Access Key ID** y el **Secret Access Key** en un lugar seguro.
- ⚠️ **Estas llaves son como la contraseña de tu casa. NUNCA las escribas en el código ni las subas a GitHub.**

### 3. Instala y configura la AWS CLI
- Instala desde **https://aws.amazon.com/cli/** (Windows, macOS o Linux).
- Verifica y configura:
  ```bash
  aws --version
  aws configure        # pega tu Access Key, Secret, región us-east-1, formato json
  ```

### 4. Sube tu data al espejo cloud
Con tu `data/raw/` poblado y desde la raíz del repo:
```bash
export ALUMNO="tu-nombre"                          # define tu identificador
bash clases/clase-01/material/aws/aws_setup_s3.sh  # crea tu bucket y sube las tablas
```
El script crea `dpl1046-tu-nombre-datalake`, lo cierra al público (seguridad) y sube cada tabla a `raw/`.

---

## Seguridad: lo no negociable

- **Nunca** subas tus Access Keys a Git. El `.gitignore` ya bloquea `.env`, `.aws/` y `*.pem`, pero la responsabilidad final es tuya.
- Usa `aws configure` (que guarda las llaves fuera del proyecto) o variables de entorno; jamás credenciales escritas dentro de un `.py`.
- En entornos más avanzados se usan **IAM Roles** (permisos asignados a la máquina) en vez de llaves. Lo veremos.

---

## Costos

Para el uso del curso (subir unos megas a S3), el Free Tier cubre prácticamente todo. En la Unidad 2 aprenderás a estimar y controlar el gasto en la nube, que es parte del oficio del ingeniero de datos.

> ¿Dudas? En la Unidad 2 vemos esto en detalle y en vivo. Por ahora, basta con que entiendas el concepto del espejo en la nube.
