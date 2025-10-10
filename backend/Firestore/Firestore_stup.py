import firebase_admin
from firebase_admin import credentials, firestore

# Inicializa o Firebase 
cred = credentials.Certificate("backend/firestore_key.json")
firebase_admin.initialize_app(cred)

# Cliente Firestore
db = firestore.client()
