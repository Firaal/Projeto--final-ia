import unittest
from app import app

class TestSystem(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    # Teste de acesso à página inicial
    def test_index_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"BebaAI", response.data)

    # Teste de envio do formulário com dados válidos
    def test_form_submission(self):
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
        self.assertIn(b"resultado", response.data)

    # Teste de erro no envio do formulário com dados incompletos
    def test_form_submission_error(self):
        form_data = {"sexo": "0"}  # Dados incompletos
        response = self.client.post("/processar", data=form_data)
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
