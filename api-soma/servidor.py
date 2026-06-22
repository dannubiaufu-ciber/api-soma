"""
Horario 1 - O primeiro servidor Flask (GET/api/soma)

Processo: o navegador (cliente) faz uma requisicao HTTP; o servidor Flaks responde
com JSON.

"""

#Lado servidor

from flask import Flask, request, jsonify

app = Flask(__name__)

#Rota 1: GET http://127.0.0.1:5000/api/soma?a=&b=3

@app.route("/api/soma", methods=["GET"]) #O decorador diz: quando chegar requisicacao GET para o caminho /api/soma execute a funcao soma()
def soma():
    # Le os parametros 'a' e 'b' da URL (query string)
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)

    # Validacao simples (Avaliacoes seguras)
    if a is None or b is None:
        return jsonify({"erro": "Informe a e b, ex: ?a=2&b=3"}), 400
    
    return jsonify({"resultado": a + b})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)


