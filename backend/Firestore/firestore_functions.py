from Firestore.firestore_setup import db


def criar_usuario(db, nome, idade, email, papel, turma_id=None):

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
        "papel": papel,
        "turmaId": turma_id
    })

    usuario_id = usuario_ref.id # captura o ID gerado automaticamente 

    # Cria subcoleções
    usuario_ref.collection("ProgressosAulas").document("_init").set({"mensagem": "Subcoleção criada"})
    usuario_ref.collection("AtividadesEntregues").document("_init").set({"mensagem": "Subcoleção criada"})
    
    print(f"✅ Usuário '{nome}' criado com ID automático: {usuario_id}")
    return usuario_id


def criar_turma(db, nome, professor_id):

    # Valida se o professor existe e tem o papel correto
    professor_ref = db.collection("Usuarios").document(professor_id).get
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