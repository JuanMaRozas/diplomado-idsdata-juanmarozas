"""
DPL1046 · Clase 8 · test_pipeline.py
Pruebas (pytest) de las funciones de transformación y de la carga.

Córrelo con:
    pytest clases/clase-08/material/proyecto-ejemplo/ -v
"""

import sqlite3

import pandas as pd

from pipeline import calcular_ventas_semanales, calcular_ventas_mensuales, pronosticar, cargar


def datos_de_ejemplo():
    """Cuatro pedidos pequeños: tres entregados y uno cancelado."""
    pedidos = pd.DataFrame({
        "order_id": ["o1", "o2", "o3", "o4"],
        "order_status": ["delivered", "delivered", "delivered", "canceled"],
        "order_purchase_timestamp": [
            "2018-01-01 10:00:00",  # lunes de la semana 1
            "2018-01-03 10:00:00",  # misma semana 1
            "2018-01-10 10:00:00",  # semana 2 (empieza el lunes 8)
            "2018-01-02 10:00:00",  # cancelado
        ],
    })
    items = pd.DataFrame({
        "order_id": ["o1", "o2", "o3", "o4"],
        "price": [100, 50, 200, 999],
    })
    return pedidos, items


# ---------- calcular_ventas_semanales ----------
def test_ignora_pedidos_no_entregados():
    pedidos, items = datos_de_ejemplo()
    ventas = calcular_ventas_semanales(pedidos, items, 10)
    assert ventas["ventas_clp"].sum() == 3500  # no incluye los 999 del cancelado


def test_convierte_reales_a_pesos():
    pedidos, items = datos_de_ejemplo()
    ventas = calcular_ventas_semanales(pedidos, items, 10)
    assert ventas.loc[ventas["semana"] == "2018-01-08", "ventas_clp"].iloc[0] == 2000  # 200 x 10


def test_suma_pedidos_de_la_misma_semana():
    pedidos, items = datos_de_ejemplo()
    ventas = calcular_ventas_semanales(pedidos, items, 10)
    assert len(ventas) == 2
    assert ventas["ventas_clp"].iloc[0] == 1500  # (100 + 50) x 10


# ---------- calcular_ventas_mensuales ----------
def ventas_semanales_ejemplo():
    return pd.DataFrame({
        "semana": ["2018-01-01", "2018-01-08", "2018-02-05"],
        "ventas_clp": [100, 300, 600],
    })


def test_un_registro_por_mes():
    mensuales = calcular_ventas_mensuales(ventas_semanales_ejemplo())
    assert len(mensuales) == 2


def test_promedio_semanal_de_cada_mes():
    mensuales = calcular_ventas_mensuales(ventas_semanales_ejemplo())
    assert mensuales.loc[mensuales["mes"] == 1, "promedio_semanal_clp"].iloc[0] == 200  # (100 + 300) / 2


def test_indice_mayor_en_el_mes_fuerte():
    mensuales = calcular_ventas_mensuales(ventas_semanales_ejemplo())
    enero = mensuales.loc[mensuales["mes"] == 1, "indice"].iloc[0]
    febrero = mensuales.loc[mensuales["mes"] == 2, "indice"].iloc[0]
    assert febrero > enero


# ---------- pronosticar ----------
def seis_semanas():
    return pd.DataFrame({
        "semana": ["2018-01-01", "2018-01-08", "2018-01-15", "2018-01-22", "2018-01-29", "2018-02-05"],
        "ventas_clp": [100, 100, 100, 100, 200, 400],
    })


def test_pronostico_tiene_las_semanas_pedidas():
    assert len(pronosticar(seis_semanas(), semanas=3)) == 3


def test_pronostico_es_el_promedio_de_las_ultimas_4_semanas():
    pronostico = pronosticar(seis_semanas(), semanas=3)
    assert (pronostico["ventas_clp_estimado"] == 200).all()  # (100 + 100 + 200 + 400) / 4 = 200


def test_pronostico_empieza_despues_de_los_datos_reales():
    pronostico = pronosticar(seis_semanas(), semanas=3)
    assert pronostico["semana"].iloc[0] > "2018-02-05"


# ---------- cargar ----------
def test_cargar_dos_veces_no_duplica(tmp_path):
    tablas = {"ventas_semanales": ventas_semanales_ejemplo()}
    carpeta = str(tmp_path) + "/"  # tmp_path: carpeta temporal que pytest crea sola
    cargar(tablas, carpeta)
    cargar(tablas, carpeta)
    conexion = sqlite3.connect(carpeta + "demanda.db")
    filas = conexion.execute("SELECT COUNT(*) FROM ventas_semanales").fetchone()[0]
    conexion.close()
    assert filas == 3
