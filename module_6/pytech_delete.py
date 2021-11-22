from pymongo import MongoClient
from pprint import pprint

url = "mongodb+srv://admin:admin@cluster0.duvph.mongodb.net/Cluster0?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech
students = db["students"]

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in students.find():
    pprint(doc)

julia = {
    "student_id" : 1010,
    "first_name" : "Julia",
    "last_name" : "Washington"
}

julia_student_id = students.insert_one(julia).inserted_id

print("Inserted student record into the students collection with document_id:")
print(julia_student_id)

print("-- DISPLAYING STUDENT TEST DOC --")
pprint(students.find_one({"student_id": 1010}))

students.delete_one({"student_id" : 1010})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in students.find():
    pprint(doc)
