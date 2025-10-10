from .Firestore_stup import db

def adicionar_aluno (aluno_dict):
    alunos_ref = db.collection('alunos')
    alunos_ref.add(aluno_dict)

def listar_alunos ():
    alunos_ref = db.collection('alunos')
    return [doc.to_dict() for doc in alunos_ref.stream()]