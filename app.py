from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

def import_model():
    try:
        with open('xgboost_treinado.pkl', 'rb') as file:
            modelo = pickle.load(file)
        return modelo
    except Exception as e:
        print(f"Erro ao carregar o modelo: {e}")
        return None

modelo = import_model()

if not modelo:
    print("Falha ao carregar o modelo. Verifique o arquivo e tente novamente.")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/processar", methods=["POST"])
def processar():
    dados = [
        float(request.form.get("sexo")),
        float(request.form.get("idade")),
        float(request.form.get("peso")),
        float(request.form.get("pressao_sistolica")),
        float(request.form.get("pressao_diastolica")),
        float(request.form.get("glicose")),
        float(request.form.get("colesterol_total")),
        float(request.form.get("colesterol_hdl")),
        float(request.form.get("colesterol_ldl")),
        float(request.form.get("triglicerideos")),
        float(request.form.get("hemoglobina")),
        float(request.form.get("proteina_urinaria")),
        float(request.form.get("creatinina_serica")),
        float(request.form.get("ast")),
        float(request.form.get("alt")),
        float(request.form.get("gama_gt")),
        float(request.form.get("estado_fumante")),
    ]
    
    resultado = modelo.predict([dados])[0]
    
    if resultado == 0:
        resultado = 'Você não consome bebibas alcóolicas'
    else:
        resultado = 'Você consome bebibas alcoólicas'

    return render_template("resultado.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)