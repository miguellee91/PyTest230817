from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.naverdb

collection = db.mycollection

# document = {"name": "John", "age": 30}
# collection.insert_one(document)
documents = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 35}]
collection.insert_many(documents)
