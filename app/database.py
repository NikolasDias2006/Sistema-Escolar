from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost:28017'
client = MongoClient(MONGO_URI)
db = client['gerenciamento_escolar']


