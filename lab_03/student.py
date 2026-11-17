class Student:

    def __init__(self, name, phone, email, group):
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group

    def __str__(self):
        return ("Student name is " + self.name + ",  Phone is " + self.phone +
                ",  Email is " + self.email + ",  Group is " + self.group)

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return (self.name, self.phone, self.email, self.group) == \
               (other.name, other.phone, other.email, other.group)