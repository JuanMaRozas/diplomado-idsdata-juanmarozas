"""
05_automatizacion_demo.py
==================================================================
DEMO DE AUTOMATIZACIÓN — funciona igual en Windows, Mac y Linux.

Muestra cómo agendar la ejecución de un pipeline para que corra
solo, sin que nadie lo toque, usando la librería `schedule`.

Instalar:
    pip install schedule

Cómo correrlo:
    python 05_automatizacion_demo.py

Para detenerlo: Ctrl + C
==================================================================
"""

import time
from datetime import datetime

import schedule
from loguru import logger

# ------------------------------------------------------------------
# La "tarea" que queremos automatizar
# En un proyecto real, aquí llamarías a tu pipeline de producción:
#   from 04_pipeline_produccion import main as ejecutar_pipeline
# ------------------------------------------------------------------
def tarea():
    ahora = datetime.now().strftime("%H:%M:%S")
    logger.success(f"✓ Pipeline ejecutado a las {ahora}")
    # En producción reemplazarías este logger por:
    #   ejecutar_pipeline()


# ------------------------------------------------------------------
# Definir el horario
# (para la demo usamos cada 10 segundos — en producción sería diario)
# ------------------------------------------------------------------
schedule.every(10).seconds.do(tarea)               # demo: cada 10 segundos

# Ejemplos reales (descomenta el que quieras probar):
# schedule.every().day.at("03:00").do(tarea)        # cada día a las 3am
# schedule.every().monday.at("08:00").do(tarea)     # cada lunes a las 8am
# schedule.every(6).hours.do(tarea)                 # cada 6 horas
# schedule.every().hour.do(tarea)                   # cada hora

# ------------------------------------------------------------------
# El loop: revisa cada segundo si hay algo que ejecutar
# ------------------------------------------------------------------
logger.info("Scheduler iniciado. Esperando el próximo turno... (Ctrl+C para detener)")
logger.info(f"Próxima ejecución: {schedule.next_run()}")

try:
    while True:
        schedule.run_pending()   # ¿hay alguna tarea que deba correr ahora?
        time.sleep(1)            # espera 1 segundo y vuelve a revisar
except KeyboardInterrupt:
    logger.info("Scheduler detenido por el usuario. Hasta mañana.")
