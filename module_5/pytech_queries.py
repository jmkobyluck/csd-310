from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.duvph.mongodb.net/Cluster0?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech
students = db["students"]

# for docs in students.find():
#     print(docs)

for docs in students.find_one({"student_id": 1007}):
    print(docs)