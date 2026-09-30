student = {"name": "Ivan", "age": 20}
print("Start dictionary:", student)

student.update({"age": 21, "city": "Chernihiv"})
print("update:", student)

del student["city"]
print("del:", student)

student.clear()
print("clear:", student)

student = {"name": "Olena", "age": 19, "city": "Kyiv"}
print("New dictionary:", student)

print("keys:", list(student.keys()))
print("values:", list(student.values()))
print("items:", list(student.items()))