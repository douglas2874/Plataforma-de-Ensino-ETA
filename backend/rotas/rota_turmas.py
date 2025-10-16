from flask import Blueprint, request, jsonify
from Firestore.firestore_setup import db
from Firestore.firestore_functions import criar_turma


# Criar um blueprint (Um grupo de rotas)
turma_bp = Blueprint("/turma", __name__)

@turma_bp.route("/criar_turma", methods=["POST"])

def criar_turma_endpoint():

    try:
        
        # Captura o JSON enviado pelo front
        dados = request.get_json

        # Armazena os tipos de dados em suas variáveis compatíveis 
        nome = dados.get("nome"),
        professor_id = dados.get("professor_id")

        # Valida campos obrigatórios
        if not nome or not professor_id:
            return jsonify({
                "status": "erro",
                "mensagem": "Campos 'nome' e 'professor_id' são obrigatórios." 
            }), 400
        
        # Chama a função de criar turmas 
        turma_id = criar_turma(db, nome, professor_id)

        # Retorna resposta JSON
        return jsonify({
            "status": "Sucesso",
            "mensagem": f"Turma '{nome}' criada com sucesso!",
            "turma_id": turma_id
        }), 201
    
    except Exception as e:
        return jsonify({
            "status": "erro",
            "mensagem": str(e)
        }), 500
