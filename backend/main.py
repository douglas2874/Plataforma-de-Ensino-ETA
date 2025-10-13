from Firestore.firestore_setup import db # Conexão já inicializada 
from Firestore.firestore_functions import criar_usuario # Função para criar usuários

# Chamada da função
usuario_id = criar_usuario(
    db = db,
    nome = "Douglas Borges",
    idade = "21",
    email="douglasborgestaj@gmail.com",
    papel="coordenador",
    turma_id="turma_01"
)
