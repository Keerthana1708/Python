dog={}
print(dog)

dogs={
    "name":"Shinchu",
    "color":"White",
    "breed":"German shepherd",
    "age": 2,
    "legs":4
}
print(dogs)

student ={
    "first_name":"Keerthana",
    "last_name":"Padubidre",
    "gender":"Female",
    "Age":22,
    "MaritalStatus":"Single",
    "skills":["Java","C++"],
    "Country":"India",
    "City":"Bangalore",
    "Address":"Chokanahalli,Thanisandra"
}
print(student)

n=len(student)
print(n)

print(student["skills"])
print(type(student["skills"]))

student["skills"].append("SpringBoot")
student["skills"].append("Python")
print(student["skills"])

new = list(student.keys())
print(new)

values = list(student.values())
print(values)

student_tuples = list(student.items())
print(student_tuples)

student.__delitem__("Age")
print(student)

del student
print(student)