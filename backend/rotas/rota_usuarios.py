from flask import Blueprint, request, jsonify
from Firestore.firestore_setup import db
from Firestore.firestore_functions import criar_usuario

# Cria o blueprint (um grupo de rotas)
usuarios_bp = Blueprint("/usuarios", __name__)

@usuarios_bp.route("/criar_usuario", methods=["POST"])
def criar_usuario_endpoint():

    
    try:

        #Captura os dados JSON enviados pelo front-end e armazena em 'dados'.
        dados = request.get_json()

        #Separa cada um dos dados e armazena respectivamente em suas variáveis compatíveis.
        nome = dados.get("nome")
        idade = dados.get("idade")
        email = dados.get("email")
        papel = dados.get("papel")
        turma_id = dados.get("turma_id")

        # Chama a função que cria no banco e passa os parâmetros recolhidos e armazenados nas variáveis 
        usuario_id = criar_usuario(db, nome, idade, email, papel, turma_id)

        # retorna uma resposta em JSON 
        return jsonify({
            "status": "Sucesso",
            "mensagem": f"Usuário '{nome}' criado com sucesso!",
            "usuario_id": usuario_id
        }), 201
    
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
        return jsonify({
            "status": "erro",
            "mensagem": str(e)
        }), 500

        


