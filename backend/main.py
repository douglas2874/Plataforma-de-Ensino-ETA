from flask import Flask, request, jsonify 
 #Importa as principais ferramentas do flask respectivamente para criar aplicação, acessa as requisições enviadas pelo cliente, converte dados do python para formato JSON e gera a resposta HTTP
from Firestore.firestore_setup import db
 #Importa variável com a ferramenta que permite manipular o banco de dados
from Firestore.firestore_functions import criar_usuario
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
