from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.duvph.mongodb.net/Cluster0?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech

print("-- Pytech Collection List --")
for coll in db.list_collection_names():
    print(coll)