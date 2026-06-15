"""
DPL1046 · Clase 3 · test_clase3.py
---------------------------------------------------------------------------
Tests para las funciones puras del Script 5 (05_refactor_olist.py).
Demuestra pytest en clase: cada test verifica un comportamiento.

Ejecutar desde la carpeta de la clase:
    pytest -v test_clase3.py

Idea pedagógica: romper una función a propósito y volver a correr,
para ver cómo pytest detecta el error exacto.
---------------------------------------------------------------------------
"""
import sys
from pathlib import Path

import pandas as pd
import pytest

# Permite importar el script aunque pytest se corra desde otra carpeta
sys.path.insert(0, str(Path(__file__).parent))
from importlib import import_module
mod = import_module("05_refactor_olist")
clasificar_resena = mod.clasificar_resena
normalizar_estado = mod.normalizar_estado
contar_resenas_negativas_con_texto = mod.contar_resenas_negativas_con_texto


# ─── clasificar_resena ───────────────────────────────────────────────────
class TestClasificarResena:
    def test_una_estrella_es_negativa(self):
        assert clasificar_resena(1) == "negativa"

    def test_dos_estrellas_es_negativa(self):
        assert clasificar_resena(2) == "negativa"

    def test_tres_estrellas_es_neutra(self):
        assert clasificar_resena(3) == "neutra"

    def test_cinco_estrellas_es_positiva(self):
        assert clasificar_resena(5) == "positiva"

    def test_score_nulo_lanza_error(self):
        with pytest.raises(ValueError):
            clasificar_resena(float("nan"))


# ─── normalizar_estado ───────────────────────────────────────────────────
class TestNormalizarEstado:
    def test_quita_espacios_y_baja(self):
        assert normalizar_estado("  Delivered  ") == "delivered"

    def test_ya_normalizado_no_cambia(self):
        assert normalizar_estado("shipped") == "shipped"

    def test_tipo_invalido_lanza_error(self):
        with pytest.raises(TypeError):
            normalizar_estado(123)


# ─── contar_resenas_negativas_con_texto ──────────────────────────────────
class TestContarResenas:
    @pytest.fixture
    def reviews_sample(self):
        """DataFrame mínimo con casos de borde controlados."""
        return pd.DataFrame([
            {"review_score": 1, "review_comment_message": "Pésimo"},     # cuenta
            {"review_score": 2, "review_comment_message": "Llegó tarde"},# cuenta
            {"review_score": 3, "review_comment_message": "Normal"},     # cuenta (<=3)
            {"review_score": 5, "review_comment_message": "Excelente"},  # no (positiva)
            {"review_score": 1, "review_comment_message": None},         # no (sin texto)
            {"review_score": None, "review_comment_message": "Sin nota"},# no (score nulo)
        ])

    def test_cuenta_negativas_con_texto(self, reviews_sample):
        # Esperado: filas 1, 2 y 3 → 3
        assert contar_resenas_negativas_con_texto(reviews_sample) == 3

    def test_umbral_mas_estricto(self, reviews_sample):
        # umbral=2 → solo filas 1 y 2 (score 3 ya no entra) → 2
        assert contar_resenas_negativas_con_texto(reviews_sample, umbral=2) == 2

    def test_dataframe_vacio_retorna_cero(self):
        vacio = pd.DataFrame(columns=["review_score", "review_comment_message"])
        assert contar_resenas_negativas_con_texto(vacio) == 0
