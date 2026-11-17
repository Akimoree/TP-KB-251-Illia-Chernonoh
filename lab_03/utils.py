import csv

from student import Student

FIELD_NAMES = ["Name", "Phone", "Email", "Group"]


class StudentFile:

    def __init__(self, fileName):
        self.fileName = fileName

    def load(self, studentList):
        studentList.clear()
        with open(self.fileName, newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                studentList.add(Student(row["Name"], row["Phone"],
                                        row["Email"], row["Group"]))

    def save(self, studentList):
        with open(self.fileName, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
            writer.writeheader()
            for item in studentList:
                writer.writerow({"Name": item.name, "Phone": item.phone,
                                 "Email": item.email, "Group": item.group})