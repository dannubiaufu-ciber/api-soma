import requests

URL = "http://127.0.0.1:5000/api/soma"

#Agora os dados vao no CORPO da requisicao (JSON)
corpo = {"a": 10, "b": 7}

#Parametros que viajam no CABECALHO (header)
cabecalhos = {"X-Cliente": "Dannubia"}

resposta = requests.post(URL, json=corpo, headers=cabecalhos)

print("Status:", resposta.status_code)
print("Corpo (JSON):", resposta.json())

#Esperado: {'resultado': 17, 'chamado_por': 'turma_ciberseguranca'}


