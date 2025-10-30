""" import requests

url = "http://127.0.0.1:5000/usuarios/criar_usuario"

dados = {
    "nome": "Douglas Borges",
    "idade": 21,
    "email": "douglasborgestaj@gmail.com",
    "senha": "douglas123",
    "papel": "professor",
    "turma_id": None
}


resposta = requests.post(url, json=dados)
print(resposta.json()) """

import requests

url = "http://127.0.0.1:5000/teste/criar_teste"

dados = {
    "teste": "ok"
}

resposta = requests.post(url, json=dados)
print(resposta.json())