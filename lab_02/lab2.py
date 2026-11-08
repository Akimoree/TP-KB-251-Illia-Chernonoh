import csv
from sys import argv

students = []


def loadFromCsv(fileName):
    students.clear()
    with open(fileName, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["Name"], "phone": row["Phone"],
                             "email": row["Email"], "group": row["Group"]})
    students.sort(key=lambda item: item["name"])
    return


def saveToCsv(fileName):
    with open(fileName, "w", newline="", encoding="utf-8") as file:
        fieldNames = ["Name", "Phone", "Email", "Group"]
        writer = csv.DictWriter(file, fieldnames=fieldNames)
        writer.writeheader()
        for item in students:
            writer.writerow({"Name": item["name"], "Phone": item["phone"],
                             "Email": item["email"], "Group": item["group"]})
    return


def printAllList():
    for elem in students:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + \
                      ",  Email is " + elem["email"] + ",  Group is " + elem["group"]
        print(strForPrint)
    return


def findInsertPosition(name):
    
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    return insertPosition


def findPosition(name):
    
    for item in students:
        if name == item["name"]:
            return students.index(item)
    return -1


def addElement(name, phone, email, group):
    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    insertPosition = findInsertPosition(name)
    students.insert(insertPosition, newItem)
    return


def removeElement(name):
    deletePosition = findPosition(name)
    if deletePosition == -1:
        return False
    del students[deletePosition]
    return True


def changeElement(name, newName, newPhone, newEmail, newGroup):
    
    updatePosition = findPosition(name)
    if updatePosition == -1:
        return False

    oldItem = students[updatePosition]
    if newName == "":
        newName = oldItem["name"]
    if newPhone == "":
        newPhone = oldItem["phone"]
    if newEmail == "":
        newEmail = oldItem["email"]
    if newGroup == "":
        newGroup = oldItem["group"]

    del students[updatePosition]
    addElement(newName, newPhone, newEmail, newGroup)
    return True


def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    addElement(name, phone, email, group)
    print("New element has been added")
    return


def deleteElement():
    name = input("Please enter name to be deleted: ")
    if removeElement(name):
        print("Element has been deleted")
    else:
        print("Element was not found")
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    updatePosition = findPosition(name)
    if updatePosition == -1:
        print("Element was not found")
        return

    oldItem = students[updatePosition]
    print("Leave the field empty if you do not want to change it")
    newName = input("Please enter new student name [" + oldItem["name"] + "]: ")
    newPhone = input("Please enter new student phone [" + oldItem["phone"] + "]: ")
    newEmail = input("Please enter new student email [" + oldItem["email"] + "]: ")
    newGroup = input("Please enter new student group [" + oldItem["group"] + "]: ")

    changeElement(name, newName, newPhone, newEmail, newGroup)
    print("Element has been updated")
    return


def main():
    if len(argv) < 2:
        print("Please specify the csv file name: python lab2.py lab2.csv")
        return
    fileName = argv[1]
    try:
        loadFromCsv(fileName)
    except FileNotFoundError:
        print("File was not found: " + fileName)
        return

    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                saveToCsv(fileName)
                print("Data has been saved to " + fileName)
                print("Exit()")
                break
            case _:
                print("Wrong chouse")
    return


if __name__ == "__main__":
    main()