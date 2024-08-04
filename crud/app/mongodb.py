from crud.settings import MONGODB_URI
from pymongo import MongoClient

client = MongoClient(MONGODB_URI)
db = client["crudappdb"]

def get_collection(collection_name):
    return db[collection_name]