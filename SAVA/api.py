from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Carrega o modelo
model = joblib.load('modelo_vendas.pkl')

# Endpoint de previsão
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Recebe os dados da requisição
        data = request.get_json()
        
        # Verifica se os dados foram recebidos corretamente
        if not data:
            return jsonify({"error": "Nenhum dado foi recebido. Verifique a requisição."}), 400
        
        # Converte os dados para um DataFrame
        df = pd.DataFrame([data])
        
        # Faz a previsão
        prediction = model.predict(df)
        
        # Retorna a previsão como JSON
        return jsonify({'prediction': prediction[0]})
    
    except Exception as e:
        # Retorna o erro como JSON
        return jsonify({"error": str(e)}), 500

# Manipulador para erros gerais
@app.errorhandler(Exception)
def handle_exception(e):
    response = {"error": str(e)}
    return jsonify(response), 500

if __name__ == '__main__':
    app.run(debug=True)
