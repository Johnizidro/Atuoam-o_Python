from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

def simulador_processamento():
    time.sleep(0.1)


@app.route('/')
def pagina_principal():
    simulador_processamento()
    return jsonify({"Mensagem": "Página Inicial"})

@app.route('/dados/busca')
def buscar_dados():
    simulador_processamento()
    return jsonify({"Resultado": ["item1", "iten2", "iten3"]})

@app.route('/dados/busca/complexa')
def buscar_dados_complexos():
    simulador_processamento()
    return jsonify({ "resultado": [{"id":i, "valor": random.radiant(1,1000)} for i in range(5)]})

if __name__ == '__main__':
    app.run(port=8000)


