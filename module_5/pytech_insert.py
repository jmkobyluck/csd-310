from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.duvph.mongodb.net/Cluster0?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech
students = db["students"]

john = {
    "student_id" : 1007,
    "first_name" : "John" 
}

jane = {
    "student_id" : 1008,
    "first_name" : "Jane"
}

josh = {
    "student_id" : 1009,
    "first_name" : "Josh"
}

john_student_id = students.insert_one(john).inserted_id
jane_student_id = students.insert_one(jane).inserted_id
josh_student_id = students.insert_one(josh).inserted_id

print(john_student_id, jane_student_id, josh_student_id)