from flask import Flask, jsonify 
from rotas import blueprints


# Cria o objeto principal da aplicação Flask. É com ele que se organiza as rotas vinculando o front com o back (API)
app = Flask(__name__)

# Registra todos os blueprint automaticamente no app
for bp in blueprints:
    app.register_blueprint(bp)

@app.route("/", methods=["GET"])
def home():
    return {"mensagem": "API do sistema acadêmico está rodando!"}

if __name__ == "__main__":
    app.run(debug=True)


    