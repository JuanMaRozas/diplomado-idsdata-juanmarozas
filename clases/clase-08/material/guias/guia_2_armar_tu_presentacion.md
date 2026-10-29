# Guía 2 de 3 — Cómo armar tu presentación del proyecto

**DPL1046 · Clase 8 · Para repasar en casa, a tu ritmo.**

En la Clase 9 cada pareja presenta su proyecto integrador: **15 minutos de presentación + 5 de preguntas**, con **demo en vivo** y la participación de **ambos integrantes**. Esta guía te ayuda a armar tu presentación con el **template del curso** (`template_presentacion_proyecto.pptx`, en `clases/clase-03/material/`), usando como modelo la presentación del proyecto de ejemplo que viste en la Clase 8.

> **Idea central:** cada slide responde **una pregunta**. Si una slide no responde su pregunta, sobra o falta algo.

---

## 1. Las 9 slides, una por una

| # | Slide | Min | Responde | Qué poner |
|-|----------|--|------------|----------------|
| 1 | **Portada** | 0,5 | ¿Quiénes y qué proyecto? | Título claro, nombres de la pareja, curso. |
| 2 | **Problema de negocio** | 2 | ¿Qué pregunta responde y para quién? | Una pregunta, quién la usa y por qué importa. |
| 3 | **Los datos** | 2 | ¿De dónde salen y qué calidad tienen? | Fuentes (≥2), tamaño, qué limpiaste y qué plan B tienes. |
| 4 | **Arquitectura** | 2 | ¿Cómo fluye: entrada → proceso → salida? | Un diagrama de cajas simple (extraer, transformar, cargar). |
| 5 | **Demo en vivo** | 3 | ¿Funciona? | Un comando, el resultado en pantalla y los tests. |
| 6 | **Resultados** | 2 | ¿Qué encontraste? | Cifras clave y un gráfico o tabla simple. |
| 7 | **Calidad y buenas prácticas** | 1 | ¿Cómo se cuida el código? | Funciones, errores, logging, tests, `config.yaml`, README. |
| 8 | **Valor de negocio** | 1,5 | ¿Qué decisión permite? | La decisión, el impacto y **una limitación** dicha con honestidad. |
| 9 | **Aprendizajes e IA** | 1 | ¿Qué aprendieron y cómo usaron IA? | Aprendizajes y ejemplos reales de uso de IA (ver sección 4). |

## 2. Cómo lo hizo el proyecto de ejemplo

| Slide | En el ejemplo |
|-------|--------------------|
| Problema | ¿Cuántas ventas esperamos en las próximas 8 semanas? Para el equipo de compras. |
| Datos | Pedidos e ítems de Olist (CSV) + dólar (API, con respaldo). Solo pedidos entregados. |
| Arquitectura | Tres cajas: Extraer → Transformar → Cargar; abajo `pipeline.py`, `config.yaml` y `tests/`. |
| Demo | `python pipeline.py`, correrlo otra vez (0 filas nuevas) y `pytest tests -v`. |
| Resultados | Ventas totales, promedio semanal, semana más fuerte y un gráfico de estacionalidad por mes. |
| Calidad | 4 tests, logging, `try/except` con respaldo, config externa, carga sin duplicar. |
| Valor | Comprar inventario **antes** de noviembre; limitación: modelo simple, sin promociones. |
| Aprendizajes e IA | Separar extraer/transformar/cargar facilita probar; qué corrigieron de la IA. |

## 3. La demo en vivo: cómo evitar sorpresas

- **Ensáyala completa** con tu pareja, cronometrada (3 minutos).
- Deja el **entorno activo** y la terminal **en la carpeta de tu proyecto** antes de empezar.
- **Corre el pipeline una vez antes** de presentar, para comprobar que funciona en ese computador.
- Ten un **plan B**: capturas de pantalla o un video corto de la ejecución, por si falla la conexión o el computador.
- Computador **cargado**, notificaciones **silenciadas** y pestañas innecesarias cerradas.

## 4. Cómo hablar de la IA con honestidad

La IA es tu **copiloto**, no tu piloto: puedes y se espera que la uses, pero **debes entender y poder explicar cada parte** de lo que entregas. En la slide 9 y en las preguntas, cuenta:

- **Qué le pediste** (por ejemplo: "un esqueleto de la función de limpieza").
- **Qué corrigió o rechazó tu pareja** (por ejemplo: "propuso guardar siempre con `append`; lo cambiamos para no duplicar semanas").
- **Cómo comprobaste** que el resultado era correcto (un test, un resultado conocido, revisar a mano).

Cualquiera de los dos puede ser interrogado sobre **cualquier línea** del código.

## 5. Preguntas que te pueden hacer

| Pregunta | Cómo prepararte |
|---|---|
| ¿Qué hace esta línea? (elegida al azar) | Lee tu código completo; ambos deben poder explicar cualquier parte. |
| ¿Qué pasa si la fuente de datos falla? | Respóndela con tu `try/except`, el plan B y el log. |
| ¿Cómo sabes que el resultado es correcto? | Respóndela con tus tests y con una comprobación a mano de una cifra. |
| ¿Qué decisión de negocio permite tu resultado? | Ten una frase lista: "con esto, el equipo puede decidir…". |
| ¿Qué parte hizo la IA y qué corregiste tú? | Ten dos ejemplos concretos. |

## 6. Checklist de entrega

- [ ] Carpeta del proyecto con el pipeline, scripts organizados.
- [ ] Corre de principio a fin **con un comando**.
- [ ] ≥2 tablas o fuentes integradas.
- [ ] Validación + `try/except` + logging.
- [ ] Tests con `pytest` (≥3 por función de transformación).
- [ ] `requirements.txt` y README claro.
- [ ] **Sin claves en el código** (usa `.env`, que nunca se sube a Git).
- [ ] Presentación de 9 slides, de 15 minutos, ensayada.

> **Si te falta algo, prioriza:** que corra de punta a punta, que tenga ≥2 fuentes y que puedas explicarlo. **Es mejor un proyecto simple que funciona que uno ambicioso que no corre.**

## 7. Errores frecuentes

- **Slides con mucho texto.** Una idea por slide; el detalle lo cuentas tú.
- **Mostrar solo código.** Cuenta primero el problema y el resultado; el código es la prueba, no la historia.
- **Resultados sin decisión.** Un número sin "¿y qué hacemos con esto?" no convence.
- **Solo habla uno.** Ambos presentan y ambos responden.
- **Pasarse de tiempo.** Cronometra: 15 minutos son 15 minutos.

## 8. Cómo se evalúa

| Criterio | Peso |
|---|---|
| Funcionalidad | 35% |
| Calidad del código | 30% |
| Buenas prácticas | 15% |
| Presentación y valor de negocio | 20% |

Aprobación: nota 4,0. Más detalle en `proyecto-integrador.md` y en `rubrica_y_temas.html` (Clase 3).
