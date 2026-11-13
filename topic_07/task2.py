class Plain:
    def __init__(self, value):
        self.value = value


class Book:
    def __init__(self, title, author):
        
        self.title = title
        self.author = author

    def __str__(self):
        
        return f"Book '{self.title}' by {self.author}"

    def __repr__(self):
        
        return f"Book({self.title!r}, {self.author!r})"


plain = Plain(5)
print("Without __str__:", plain)
print("Attribute value:", plain.value)

book = Book("Kobzar", "Taras Shevchenko")
print("print(book):", book)
print("str(book):", str(book))
print("repr(book):", repr(book))

books = [book, Book("Zakhar Berkut", "Ivan Franko")]
print("List of books:", books)
print("Book title:", books[1].title)