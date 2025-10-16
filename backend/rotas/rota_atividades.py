from flask import request, Blueprint, jsonify
from Firestore.firestore_setup import db
from Firestore.firestore_functions import criar_atividade

atividades_bp = Blueprint("/atividades", __name__)
@atividades_bp.route("/criar_atividade", methods = ["POST"])

def criar_aula_endpoint():

    try:

        dados = request.get_json()

        titulo = dados.get("titulo")
        descricao = dados.get("descricao")
        arquivoUrl = dados.get("arquivoUrl")
        professor_id = dados.get("professor_id")
        turma_id = dados.get("turma_id")
        data_Entrega = dados.get("data_Entrega")
        data_Postagem = dados.get("data_Postagem")

        atividade_id = criar_atividade(db, titulo, descricao, arquivoUrl, professor_id,turma_id, data_Entrega, data_Postagem)

        return jsonify({
            "status": "Sucesso",
            "mensagem": f"A atividade '{titulo}' foi postada com sucesso",
            "atividade_id": atividade_id
        }), 201
    
    except Exception as e:
        return jsonify({
            "status": "erro",
            "mensagem": str(e)
        }), 500