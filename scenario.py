class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

        if price >= 500:
            self.category = "Premium"
        else:
            self.category = "Standard"

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Category:", self.category)
        print("------------------------")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("===== Library Books =====")
        for book in self.books:
            book.display()


# Creating Library object
library = Library()

# Adding books
library.add_book(Book(101, "C++ Programming", "Bjarne Stroustrup", 650))
library.add_book(Book(102, "Data Structures", "Seymour Lipschutz", 450))
library.add_book(Book(103, "Database Systems", "Raghu Ramakrishnan", 700))

# Displaying all books
library.display_books()
