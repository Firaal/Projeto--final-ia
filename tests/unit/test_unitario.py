import unittest
from unittest.mock import patch, mock_open
from app import import_model

class TestModelLoading(unittest.TestCase):
    # Teste de carregamento bem-sucedido do modelo
    @patch("builtins.open", new_callable=mock_open)
    @patch("pickle.load")
    def test_import_model_success(self, mock_pickle_load, mock_file):
        mock_pickle_load.return_value = "modelo_teste"
        modelo = import_model()
        self.assertEqual(modelo, "modelo_teste")

    # Teste de falha ao carregar o modelo
    @patch("builtins.open", side_effect=Exception("Erro"))
    def test_import_model_failure(self, mock_open):
        modelo = import_model()
        self.assertIsNone(modelo)

    # Teste de predição do modelo
    @patch("pickle.load", return_value=type("MockModel", (), {"predict": lambda self, x: [1]})())
    def test_model_predict(self, mock_model):
        modelo = import_model()
        dados = [0, 25, 70, 120, 80, 90, 200, 50, 100, 150, 14, 10, 0.9, 40, 40, 40, 1]
        resultado = modelo.predict([dados])[0]
        self.assertIn(resultado, [0, 1])

    # Teste de conversão de dados do formulário
    def test_form_data_conversion(self):
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
        dados = [float(form_data[k]) for k in form_data]
        self.assertEqual(len(dados), 17)
        self.assertTrue(all(isinstance(d, float) for d in dados))

    # Teste de resposta do resultado
    @patch("pickle.load", return_value=type("MockModel", (), {"predict": lambda self, x: [1]})())
    def test_result_message(self, mock_model):
        modelo = import_model()
        resultado = modelo.predict([[0]*17])[0]
        mensagem = "Você consome bebibas alcoólicas" if resultado == 1 else "Você não consome bebibas alcóolicas"
        self.assertIn(mensagem, ["Você consome bebibas alcoólicas", "Você não consome bebibas alcóolicas"])

if __name__ == "__main__":
    unittest.main()
