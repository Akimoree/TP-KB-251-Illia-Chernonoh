


list = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@gmail.com", "group": "KB-252"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@gmail.com", "group": "KB-241"},
    {"name": "Jon", "phone": "0631234567", "email": "jon@gmail.com", "group": "KB-242"},
    {"name": "Zak", "phone": "0631234567", "email": "zak@gmail.com", "group": "KB-251"}
]


def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + \
                      ",  Email is " + elem["email"] + ",  Group is " + elem["group"]
        print(strForPrint)
    return


def findInsertPosition(name):
    # find insert position in the sorted list
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    return insertPosition


def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    insertPosition = findInsertPosition(name)
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return


def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    updatePosition = -1
    for item in list:
        if name == item["name"]:
            updatePosition = list.index(item)
            break
    if updatePosition == -1:
        print("Element was not found")
        return

    oldItem = list[updatePosition]
    print("Leave the field empty if you do not want to change it")
    newName = input("Please enter new student name [" + oldItem["name"] + "]: ")
    newPhone = input("Please enter new student phone [" + oldItem["phone"] + "]: ")
    newEmail = input("Please enter new student email [" + oldItem["email"] + "]: ")
    newGroup = input("Please enter new student group [" + oldItem["group"] + "]: ")

    
    if newName == "":
        newName = oldItem["name"]
    if newPhone == "":
        newPhone = oldItem["phone"]
    if newEmail == "":
        newEmail = oldItem["email"]
    if newGroup == "":
        newGroup = oldItem["group"]

    newItem = {"name": newName, "phone": newPhone, "email": newEmail, "group": newGroup}

   
    del list[updatePosition]
    insertPosition = findInsertPosition(newName)
    list.insert(insertPosition, newItem)
    print("Element has been updated")
    return


def main():
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
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()