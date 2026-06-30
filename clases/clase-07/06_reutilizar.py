"""
06_reutilizar.py  ·  Clase 7 · Buena práctica: importar funciones de otro archivo
---------------------------------------------------------------------------------
ESTE ARCHIVO ENSEÑA LA LECCIÓN DE  `if __name__ == "__main__":`

Cuando arriba escribimos:

    from indicadores import pedir_indicador, a_tabla

Python ABRE el archivo indicadores.py para sacar esas dos funciones. Pero fíjate:
NO viste correr la demo de indicadores.py (no apareció "Corriendo indicadores.py
como PROGRAMA PRINCIPAL"). ¿Por qué? Porque esa demo está protegida por:

    if __name__ == "__main__":
        main()

La variable mágica __name__ vale:
  • "__main__"        cuando ejecutas el archivo directamente (python indicadores.py)
  • el nombre del módulo ("indicadores")  cuando OTRO archivo lo importa.

Así, indicadores.py sirve para DOS cosas a la vez:
  1) ejecutarse solo (corre su main),
  2) prestar sus funciones a otros archivos (sin correr su main).

Esa es la buena práctica: pon tus funciones reutilizables en un módulo, protégelo
con el if, e impórtalas donde las necesites. NO copies y pegues el mismo código.
"""

from loguru import logger
from indicadores import pedir_indicador, a_tabla   # importar NO corre la demo del módulo


def main():
    # Pista visual de la lección: aquí __name__ vale "__main__"
    logger.info(f"En 06_reutilizar.py, __name__ vale: {__name__!r}")
    logger.info("Por eso ESTA main() sí corre. La de indicadores.py NO corrió al importarlo.")

    # Reutilizamos las funciones del módulo sin reescribirlas:
    datos = pedir_indicador("dolar")
    tabla = a_tabla(datos, "dolar_clp")

    logger.success("Reutilicé pedir_indicador() y a_tabla() sin copiar una sola línea.")
    print("\nÚltimos 3 días del dólar (traídos con código reutilizado):")
    print(tabla.tail(3).to_string(index=False))


if __name__ == "__main__":
    main()
