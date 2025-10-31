from flask import request, Blueprint, jsonify
from Firestore.firestore_setup import db
from Firestore.firestore_functions import criar_aula

aulas_bp = Blueprint("aulas", __name__, url_prefix="/aulas")

@aulas_bp.route("criar_aula", methods=["POST"],)

def criar_aula_endpoint ():
    try:
        
        # Diagnostico - Ver o que realmente chega da requisição
        print("Content-Type:", request.content_type)
        print("Corpo Bruto (request.data)", request.data)
        print("get_json(silent=True)", request.get_json(silent=True))

        #Captura o JSON enviado pelo front 
        dados = request.get_json()

        # Armazena cada dado em sua variável compatível
        titulo = dados.get("titulo")
        descricao = dados.get("descricao")
        videoUrl = dados.get("videoUrl")
        professor_id = dados.get("professor_id")
        turma_id = dados.get("turma_id")
        data_postagem = dados.get("data_postagem")

        # Chama a função que cria no banco e passa os parâmetros recolhidos e armazenados nas variáveis 
        aula_id = criar_aula(db, titulo, descricao, videoUrl, professor_id, turma_id)


        return jsonify({
            "status": "Sucesso",
            "mensagem": f"A aula '{titulo} foi criada com sucesso",
            "aula_id": aula_id
        }), 201
    
    except Exception as e:
        return jsonify({
            "status": "erro",
            "mensagem": str(e)
        }), 500
