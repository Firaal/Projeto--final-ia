import unittest
from unittest.mock import patch
from app import app, import_model

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    # Teste da integração do formulário com o modelo
    @patch("pickle.load", return_value=type("MockModel", (), {"predict": lambda self, x: [1]})())
    def test_form_to_model_integration(self, mock_model):
        form_data = {
            "sexo": "0",
            "idade": "30",
            "peso": "70",
            "pressao_sistolica": "120",
            "pressao_diastolica": "80",
            "glicose": "90",
            "colesterol_total": "200",
            "colesterol_hdl": "50",
            "colesterol_ldl": "100",
            "triglicerideos": "150",
            "hemoglobina": "14",
            "proteina_urinaria": "10",
            "creatinina_serica": "0.9",
            "ast": "40",
            "alt": "40",
            "gama_gt": "40",
            "estado_fumante": "1"
        }
        response = self.client.post("/processar", data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Você consome bebibas alcoólicas".encode("utf-8"), response.data)

    # Teste da página de resultados
    @patch("pickle.load", return_value=type("MockModel", (), {"predict": lambda self, x: [0]})())
    def test_results_page_render(self, mock_model):
        form_data = {
            "sexo": "0",
            "idade": "30",
            "peso": "70",
            "pressao_sistolica": "120",
            "pressao_diastolica": "80",
            "glicose": "90",
            "colesterol_total": "200",
            "colesterol_hdl": "50",
            "colesterol_ldl": "100",
            "triglicerideos": "150",
            "hemoglobina": "14",
            "proteina_urinaria": "10",
            "creatinina_serica": "0.9",
            "ast": "40",
            "alt": "40",
            "gama_gt": "40",
            "estado_fumante": "1"
        }
        response = self.client.post("/processar", data=form_data)
        self.assertIn("Você não consome bebibas alcóolicas".encode("utf-8"), response.data)

if __name__ == "__main__":
    unittest.main()
