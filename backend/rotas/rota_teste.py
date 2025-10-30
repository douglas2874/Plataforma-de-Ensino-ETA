from flask import request, Blueprint, jsonify
from Firestore.firestore_setup import db
from Firestore.firestore_functions import criar_teste

teste_bp = Blueprint("teste", __name__, url_prefix="/teste")
@teste_bp.route("/criar_teste", methods=["POST"])
def criar_teste_endpoint():

    try:
        dados = request.get_json()

        teste = dados.get("teste")

        teste_id= criar_teste(db, teste)

        return jsonify({
            "status": "Sucesso",
            "mensagem": f"O teste {teste} foi criado com sucesso.",
            "teste_id": teste_id 
        }),201
    
    except Exception as e:
        return({
            "status": "Erro",
            "mensagem": str(e)
        }), 500