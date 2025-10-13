#Arquivo de configuração e integração do Firebase Cloude Firestore
#Importa a bibliotrca e seus módulos de autenticar acesso (credentials) e usabilidade das ferramentas (firestore)
import firebase_admin
from firebase_admin import credentials, firestore

# Inicializa o Firebase 
# "Certificate" converte a chave em um objeto credencial para ser usado pelo "credential" para validar o acesso
cred = credentials.Certificate("backend/firestore_key.json")
# ".initialize_app(cred)" acessa o firestore e o banco de dados usando a credencial criada 
firebase_admin.initialize_app(cred)



# Cliente Firestore
# armazena o módulo que permite usar as funções CRUD do firestore em uma variável "db"
db = firestore.client()
