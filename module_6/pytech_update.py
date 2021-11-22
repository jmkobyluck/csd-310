from pymongo import MongoClient
from pprint import pprint

url = "mongodb+srv://admin:admin@cluster0.duvph.mongodb.net/Cluster0?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech
students = db["students"]

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
pprint(students.find_one({"student_id": 1007}))

update = students.update_one({"student_id" : 1007}, {"$set" : {"last_name" : "Doe"}})

print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
pprint(students.find_one({"student_id": 1007}))
