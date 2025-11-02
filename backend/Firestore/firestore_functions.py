from Firestore.firestore_setup import db
from datetime import datetime 
import bcrypt 

#função teste
def criar_teste(db,teste):
    
    teste_ref= db.collettion("Teste").document()
    teste_ref.set({
        "teste": teste
    })

    teste_id = teste_ref.id
    print(f"Teste criado com sucesso com id {teste_id} ")
    return teste_id


#Função para criar usuários 
def criar_usuario(db, nome, idade, email, senha, papel, turma_id=None):

    senha_hash = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt())

    # Valida se o papel escolhido existe
    
    papeis_validos = ["aluno", "professor", "coordenador"]
    if papel not in papeis_validos:
        raise ValueError(f"Papel inválido: {papel}. Deve ser um dos {papeis_validos}")
    
    # Se for aluno, valida se a turma selecionada existe
    if papel == "aluno" and turma_id:
        turma_ref = db.collection("Turmas").document(turma_id).get()
        if not turma_ref.exists:
            raise ValueError(f"Turma com ID {turma_id} não existe.")

    usuario_ref = db.collection("Usuários").document() #sem passar ID -> firestore gera um automaticamente
    usuario_ref.set({
        "nome": nome,
        "idade": idade,
        "email": email,
        "senha": senha_hash.decode("utf-8"),
        "papel": papel,
        "turma_id": turma_id
    })

    usuario_id = usuario_ref.id # captura o ID gerado automaticamente 

    # Cria subcoleções
    usuario_ref.collection("ProgressosAulas").document("_init").set({"mensagem": "Subcoleção criada"})
    usuario_ref.collection("AtividadesEntregues").document("_init").set({"mensagem": "Subcoleção criada"})
    
    print(f"✅ Usuário '{nome}' criado com ID automático: {usuario_id}")
    return usuario_id


#Função para criar turmas 
def criar_turma(db, nome, professor_id):

    # Valida se o professor existe e tem o papel correto
    professor_ref = db.collection("Usuários").document(professor_id).get()
    if not professor_ref.exists:
        raise ValueError(f"Professor com ID {professor_id} não existe.")
    if professor_ref.to_dict().get("papel") != "professor":
        raise ValueError(f"O usuário com ID {professor_id} não é um professor.")
    

    # Cria a turma com ID aleatório
    turma_ref = db.collection("Turmas").document() # ID gerado automaticamente
    turma_id = turma_ref.id

    #Define os dados da turma
    turma_ref.set({
        "nome": nome,
        "professorId": professor_id,
        "alunos": [] # array vazio inicialmente
    })

    print(f"✅ Turma '{nome}' criada com ID: {turma_id}")
    return turma_id


def criar_aula (db, titulo, descricao, videoUrl, professor_id, turma_id):
    
    # Valida se o professor existe e tem o papel correto
    professor_ref = db.collection("Usuários").document(professor_id).get()
    if not professor_ref.exists:
        raise ValueError(f"O usuário com ID {professor_id} não existe.")
    if professor_ref.to_dict().get("papel") != "professor":
        raise ValueError(f"O usuário com ID {professor_id} não é um professor ")
    
    # Verifica se a turma existe
    turma_ref = db.collection("Turmas").document(turma_id).get()
    if not turma_ref.exists:
        raise ValueError(f"A turma com o ID {turma_id} não existe.")
    
    # Cria ou acessa a coleção, cria a referencia do documento com ID aleatório
    aula_ref = db.collection("Aulas").document()
    aula_id = aula_ref.id

    # Define os dados que serão preenchidos no cadastro das aulas 
    aula_ref.set({
        "titulo": titulo,
        "descricao": descricao,
        "videoUrl": videoUrl,
        "professor_id": professor_id,
        "turma_id": turma_id,
        "data_postagem": datetime.now().isoformat() #ISO 8601 (ex: 20225-10-14T21:34:00)
    })

    print(f"Aula '{titulo} criada com o ID: {aula_id}'")
    return aula_id

    
def criar_atividade (db, titulo, descricao, arquivo_url, professor_id, turma_id, data_entrega):
    
    # Valida se o professor existe e tem o papel correto
    professor_ref = db.collection("Usuários").document(professor_id).get()
    if not professor_ref.exists:
        raise ValueError(f"O usuário com ID {professor_id} não existe.")
    if professor_ref.to_dict().get("papel") != "professor":
        raise ValueError(f"O usuário com ID {professor_id} não é um professor.")
    
    # Verifica se a turma existe 
    turma_ref = db.collection("Turmas").document(turma_id).get()
    if not turma_ref.exists:
        raise ValueError(f"A turma com ID {turma_id} não existe.")
    
    # Cria ou acessa a coleção, cria a referencia do documento com ID aleatório
    atividade_ref = db.collection("Atividades").document()
    atividade_id = atividade_ref.id
    
    # Define os dados que serão preenchidos no cadastro das atividades 
    atividade_ref.set({
        "titulo": titulo,
        "descricao": descricao,
        "arquivo_url": arquivo_url,
        "professor_id": professor_id,
        "turma_id": turma_id,
        "data_entrega": data_entrega,                   # Inserida manualmente via Front
        "data_postagem": datetime.now().isoformat()     # gerada automaticamente
    })

    print (f" Atividade '{titulo}' criada com ID: {atividade_id}")
    return atividade_id


def verificar_login(email:str , senha_digitada:str):
    try:
        # Acessa a coleção Usuários e procura a existencia de algum com o email inserido
        usuarios = db.collectio("Usuários").where("email", "==", email).get()

        if not usuarios:
            return {
                "status": "erro",
                "mensagem": "Usuário não encontrado."
            }
        
        # Com isso, caso haja dois usuários com o mesmo email, ele ira guardar apenas o primeiro encontrado
        usuario = usuarios[0].to_dict()

        #Acessa aos dados do usuário e pega a senha que esta armazenada no campo "senha"
        senha_hash_banco = usuario.get("senha")

        # compara a senha inserida pelo usuário com a senha armazenada
        senha_ok = bcrypt.checkpw(senha_digitada.encode("utf-8"), senha_hash_banco.encode("utf-8"))

        if not senha_ok:
            return{
                "status": "erro",
                "mensagem": "Senha incorreta."
            }

        # Se passou pela verificação do email e senha retorna
        return{
            "status": "sucesso",
            "usuario":{
                "nome": usuario.get("nome"),
                "email": usuario.get("email"),
                "papel": usuario.get("papel"),
                "turma_id": usuario.get("usuario_id")
            }
        }    
     
    except Exception as e:
        print("Erro ao verificar login:", e)
        return{
            "status": "erro",
            "mensagem": "Erro interno no servidor."
        }  



