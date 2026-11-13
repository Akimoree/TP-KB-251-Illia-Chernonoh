class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student name is {self.name}, age is {self.age}"


students = [
    Student("Emma", 20),
    Student("Bob", 19),
    Student("Zak", 22),
    Student("Jon", 18)
]

print("Not sorted list:")
for student in students:
    print(student)

print("Sorted by name:")
for student in sorted(students, key=lambda item: item.name):
    print(student)

print("Sorted by age:")
for student in sorted(students, key=lambda item: item.age):
    print(student)