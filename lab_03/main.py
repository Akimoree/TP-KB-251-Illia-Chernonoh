from sys import argv

from student import Student
from student_list import StudentList
from utils import StudentFile


def addNewElement(studentList):
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    studentList.add(Student(name, phone, email, group))
    print("New element has been added")


def deleteElement(studentList):
    name = input("Please enter name to be deleted: ")
    if studentList.remove(name):
        print("Element has been deleted")
    else:
        print("Element was not found")


def updateElement(studentList):
    name = input("Please enter name to be updated: ")
    position = studentList.findPosition(name)
    if position == -1:
        print("Element was not found")
        return
    old = studentList[position]
    print("Leave the field empty if you do not want to change it")
    newName = input("Please enter new student name [" + old.name + "]: ")
    newPhone = input("Please enter new student phone [" + old.phone + "]: ")
    newEmail = input("Please enter new student email [" + old.email + "]: ")
    newGroup = input("Please enter new student group [" + old.group + "]: ")
    studentList.update(name, newName, newPhone, newEmail, newGroup)
    print("Element has been updated")


def main():
    if len(argv) < 2:
        print("Please specify the csv file name: python main.py lab3.csv")
        return
    storage = StudentFile(argv[1])
    studentList = StudentList()
    try:
        storage.load(studentList)
    except FileNotFoundError:
        print("File was not found: " + argv[1])
        return

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match choice:
            case "C" | "c":
                addNewElement(studentList)
                studentList.printAll()
            case "U" | "u":
                updateElement(studentList)
                studentList.printAll()
            case "D" | "d":
                deleteElement(studentList)
                studentList.printAll()
            case "P" | "p":
                studentList.printAll()
            case "X" | "x":
                storage.save(studentList)
                print("Data has been saved to " + argv[1])
                print("Exit()")
                break
            case _:
                print("Wrong choice")


if __name__ == "__main__":
    main()