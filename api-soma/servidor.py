"""
Horario 1 - O primeiro servidor Flask (GET/api/soma)

Processo: o navegador (cliente) faz uma requisicao HTTP; o servidor Flaks responde
com JSON.

"""

#Lado servidor

from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

#Em producao, isto varia de variavel de ambiente, NUNCA no codigo!
TOKEN_VALIDO = "segredo-da-turma-123"

def requer_token(funcao):
    @wraps(funcao)
    def envoltorio(*args, **kwargs):
        cabecalho = request.headers.get("Authorization", " ")

        # 1) precisa comecar com "Bearer"
        if not cabecalho.startswith("Bearer "):
            return jsonify({"erro": "token ausente"}), 401
        
        # 2) extrai o token depois da palavra "Bearer"
        token = cabecalho.split(" ",1)[1]

        # 3) confere se o token e valido
        if token != TOKEN_VALIDO:
            return jsonify({"erro":"token invalido"}), 401
        
        return funcao(*args, **kwargs)
    return envoltorio

#Rota protegida: exige Authorization: Bearer <token>
@app.route("/api/protegido", methods=["GET"])
@requer_token

def protegido():
    return jsonify({"mensagem": "Acesso autorizado! Dados secretos aqui."})
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

@app.route("/api/soma", methods=["POST"]) 
def soma_post():
    dados = request.get_json(silent=True) or {}
    a = dados.get("a")
    b = dados.get("b")

    # Le um parametro enviado no CABECALHO (header) da requisicao
    cliente = request.headers.get("X-Cliente", "anonimo")

    if a is None or b is None:
        return jsonify({"erro": "envie a e b no corpo JSON"}), 400
    
    return jsonify({"resultado": a + b, "chamado_por": cliente})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)


