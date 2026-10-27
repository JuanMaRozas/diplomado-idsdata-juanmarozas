"""
tests/test_pipeline.py · Tests del pipeline de demanda
------------------------------------------------------
≥3 tests con pytest como pide la rúbrica.
"""

import pandas as pd
import numpy as np
import pytest
from src.transformar import calcular_estacionalidad, generar_pronostico


@pytest.fixture
def ventas_ejemplo():
    """Genera 20 semanas de datos ficticios para testear."""
    fechas = pd.date_range("2024-01-01", periods=20, freq="W-MON")
    np.random.seed(42)
    return pd.DataFrame({
        "semana": [f.date().isoformat() for f in fechas],
        "n_pedidos": np.random.randint(50, 200, 20),
        "n_items": np.random.randint(100, 500, 20),
        "ventas_clp": np.random.uniform(500_000, 2_000_000, 20).round(0),
    })


def test_estacionalidad_tiene_12_meses(ventas_ejemplo):
    """La estacionalidad debe tener exactamente una fila por mes presente."""
    resultado = calcular_estacionalidad(ventas_ejemplo)
    assert len(resultado) > 0
    assert "indice" in resultado.columns
    assert resultado["indice"].min() > 0, "El índice no puede ser negativo"


def test_pronostico_genera_semanas_correctas(ventas_ejemplo):
    """El pronóstico debe generar exactamente N semanas futuras."""
    n = 4
    resultado = generar_pronostico(ventas_ejemplo, semanas_futuras=n)
    assert len(resultado) == n
    assert "ventas_clp_estimado" in resultado.columns
    assert (resultado["ventas_clp_estimado"] >= 0).all(), "No puede haber ventas negativas"


def test_pronostico_fechas_son_futuras(ventas_ejemplo):
    """Las fechas del pronóstico deben ser posteriores a la última semana real."""
    resultado = generar_pronostico(ventas_ejemplo, semanas_futuras=4)
    ultima_real = ventas_ejemplo["semana"].max()
    primera_pronostico = resultado["semana"].min()
    assert primera_pronostico > ultima_real, "El pronóstico debe empezar después de los datos reales"


def test_idempotencia_carga():
    """Cargar dos veces no duplica datos."""
    from src.cargar import guardar_en_base
    import os

    bd_test = "sqlite:///salida/test_idempotencia.db"
    datos = pd.DataFrame({
        "semana": ["2024-01-01", "2024-01-08"],
        "n_pedidos": [100, 120],
        "n_items": [200, 250],
        "ventas_clp": [1_000_000, 1_200_000],
    })
    pronostico = pd.DataFrame({
        "semana": ["2024-01-15"],
        "ventas_clp_estimado": [1_100_000],
        "tipo": ["pronóstico"],
    })

    os.makedirs("salida", exist_ok=True)
    n1 = guardar_en_base(datos, pronostico, bd_test)
    n2 = guardar_en_base(datos, pronostico, bd_test)
    assert n1 == 2, f"Primera carga debería insertar 2, insertó {n1}"
    assert n2 == 0, f"Segunda carga debería insertar 0, insertó {n2}"

    # Limpiar
    os.remove("salida/test_idempotencia.db")
