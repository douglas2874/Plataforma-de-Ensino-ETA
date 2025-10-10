from Firestore.firestore_functions import adicionar_aluno, listar_alunos

# Teste simples
novo_aluno = {"nome": "Douglas", "idade": 21}
adicionar_aluno(novo_aluno)

print(listar_alunos)