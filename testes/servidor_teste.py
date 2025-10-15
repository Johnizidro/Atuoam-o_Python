from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

def simulador_processamento():
    time.sleep(0.1)


@app.route('/')
def pagina_principal():
    simulador_processamento()
    return jsonify({"Mensagem: Página Inicial"})

if __name__ == '__main__':
    app.run(port=8000)