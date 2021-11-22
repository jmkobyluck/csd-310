john_student_id = students.insert_one(john).inserted_id
jane_student_id = students.insert_one(jane).inserted_id
josh_student_id = students.insert_one(josh).inserted_id

print(john_student_id, jane_student_id, josh_student_id)