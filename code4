# Decorator to add stars around output
def star_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "*** " + result + " ***"
    return wrapper


class Book:
    def __init__(self, book_name):
        self.book_name = book_name

    @classmethod
    def create_book(cls, name):
        return cls(name)

    def __str__(self):
        return f"Book Name: {self.book_name}"

    @star_decorator
    def details(self):
        return f"You selected the book '{self.book_name}'. Happy Reading!"


# Main Program
book = input("Enter book name: ")

my_book = Book.create_book(book)

print("\n", my_book)
print(my_book.details())
