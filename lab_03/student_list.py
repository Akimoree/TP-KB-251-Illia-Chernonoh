from student import Student


class StudentList:

    def __init__(self):
        self._students = []

    def __len__(self):
        return len(self._students)

    def __iter__(self):
        return iter(self._students)

    def __getitem__(self, index):
        return self._students[index]

    def clear(self):
        self._students.clear()

    def names(self):
        return [item.name for item in self._students]

    def findInsertPosition(self, name):
        insertPosition = 0
        for item in self._students:
            if name > item.name:
                insertPosition += 1
            else:
                break
        return insertPosition

    def findPosition(self, name):
        for index, item in enumerate(self._students):
            if item.name == name:
                return index
        return -1

    def add(self, student):
        self._students.insert(self.findInsertPosition(student.name), student)

    def remove(self, name):
        position = self.findPosition(name)
        if position == -1:
            return False
        del self._students[position]
        return True

    def update(self, name, newName, newPhone, newEmail, newGroup):
        # empty string means "keep the old value"
        position = self.findPosition(name)
        if position == -1:
            return False
        old = self._students[position]
        updated = Student(newName or old.name, newPhone or old.phone,
                          newEmail or old.email, newGroup or old.group)
        del self._students[position]
        self.add(updated)
        return True

    def printAll(self):
        for item in self._students:
            print(item)