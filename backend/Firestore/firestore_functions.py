from Firestore.firestore_setup import db


def criar_usuario(db, nome, idade, email, papel, turma_id=None):
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
