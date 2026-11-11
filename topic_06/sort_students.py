students = [
    {"name": "Emma", "grade": 90},
    {"name": "Bob", "grade": 75},
    {"name": "Zak", "grade": 82},
    {"name": "Jon", "grade": 68}
]

print("Not sorted list:")
for item in students:
    print(item)

sorted_by_name = sorted(students, key=lambda item: item["name"])
print("Sorted by name:")
for item in sorted_by_name:
    print(item)

sorted_by_grade = sorted(students, key=lambda item: item["grade"])
print("Sorted by grade:")
for item in sorted_by_grade:
    print(item)