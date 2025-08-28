student_dict = {
    "Name": "Ling",
    "Age": 20,
    "Grades": "A"
}

print(student_dict["Name"])

student_dict["School"] = "Green High"

def print_dict(dict_name):
    print(*list("\n" + x + ": " + str(y) for x,y in dict_name.items()))

print_dict(student_dict)

student_dict["Grade"] = "A"

student_dict["Hobbies"] = ["Coding", "Watching movies"]

print_dict(student_dict)

student_dict["Grades"] = student_dict.pop("Grade")
print_dict(student_dict)

student_dict["Grades"] = {
    "Science": 95,
    "Math": 75
}
print_dict(student_dict)

student_dict["Grades"]["English"] = 90
print(f"Grades: {student_dict["Grades"]}")

students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 21}
]

students.append({"name": "Clara", "age": 19})

print("-"*9)
for student in students:
    for x, y in student.items():
        print(f"{x.capitalize()}: {y}")
    print("-"*9)

school = {
    "students": [
        {"name": "Alice", "grades": {"math": 85, "science": 92}},
        {"name": "Bob", "grades": {"math": 78, "science": 88}}
    ]
}

print(f"Alice's grade in science: {school["students"][0]["grades"]["science"]}")

print(f"Bob's math grade: {school['students'][1]["grades"]["math"]}")