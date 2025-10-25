import firebase_admin
from firebase_admin import credentials, firestore

# Inicializa o Firebase 
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)

# Cliente Firestore
# armazena o módulo que permite usar as funções CRUD do firestore em uma variável "db"
db = firestore.client()
