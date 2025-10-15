from flask import Flask, request, jsonify 
 #Importa as principais ferramentas do flask respectivamente para criar aplicação, acessar as requisições enviadas pelo cliente, converter dados do python para formato JSON e gerar a resposta HTTP
from Firestore.firestore_setup import db
 #Importa variável com a ferramenta que permite manipular o banco de dados
from Firestore.firestore_functions import criar_usuario, criar_turma, criar_aula, criar_atividade
 #Importa a função responsável por criar usuários 

app = Flask(__name__)
 #Cria o objeto principal da aplicação Flask. É com ele que registra as rotas vinculando com as funções


# Rota para criar usuário
@app.route("/criar_usuario", methods=["POST"])
 #Usa o objeto criado "app" para criar a rota da função com o end point

def criar_usuario_endpoint():
    try:
        #Captura os dados JSON enviados pelo front

        dados = request.get_json()
         #Pega os dados enviados pelo front-end
        
        nome = dados.get("nome")
        idade = dados.get("idade")
        email = dados.get ("email")
        papel = dados.get ("papel")
        turma_id = dados.get("turma_id")
         #Separa cada um dos dados recolhidos e armazena respectivamente em suas variáveis compatíveis 

        usuario_id = criar_usuario(db, nome, idade, email, papel, turma_id)
         # Chama a função no Firestore
        
        return jsonify({
            "staus": "Sucesso",
            "mensagem": f"Usuário '{nome}' criado com sucesso!",
            "usuario_id": usuario_id
        }), 201
         # Retorna uma resposta JSON
    
    except Exception as e:
        print (f"❌ Erro ao criar usuário: {e}")
        return jsonify({
            "status": "erro",
            "mensagem": str(e)
        }), 500


# Rota para criar turma 
@app.route("/criar_turma", methods = ["POST"])
 # Usa o objeto criado "app" para criar a rota da função com o end point 

def criar_turma_endpoint():
    try:
        # Captura o JSON enviado pelo front
        dados = request.get_json()
        nome = dados.get("nome")
        professor_id = dados.get("professor_id")

        # Valida campos obrigatórios 
        if not nome or not professor_id:
            return jsonify({
                "status": "erro",
                "mensagem": "Campos 'nome' e 'professor_id' são obrigatórios."
            }), 400
        
        # Chama a função de criação de turma
        turma_id = criar_turma(db, nome, professor_id)

        # Retorna resposta JSON
        return jsonify({
            "status": "sucesso",
            "mensagem": f"Turma '{nome}' criada com sucesso!",
            "turma_id": turma_id
        }), 201
    
    except ValueError as ve:
        # Erro específico de validação (ex: professor inexistente)
        return jsonify({ "status": "erro", "mensagem": "str(ve)"}), 500
    