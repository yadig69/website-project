# ! Challenge 1: Library Management System (Intermediate)
print("-- Library Management System --")
# Scenario
# Build a system to track books in a library and allow patrons to borrow or return them.
# ^ Requirements
# 1. Book Class:
class Book:
# ? Attributes: title (str), author (str), is_borrowed (bool, default False).
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
# ^ Methods:
# ? borrow(): Sets is_borrowed to True if available. Returns success/failure message.
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"Sorry {self.title} is already borrowed."
        else:
            return f" ${self.title} is available."
# return_book(): Sets is_borrowed to False. Returns confirmation.
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"Thank you for returning {self.title}!"
        else:
            return f"Error: {self.title} was not borrowed."

# ! 2. Library Class:
class Library:
# ? Attribute: books (list of Book objects).
    def __init__(self):
        self.books = []
# ^ Methods:
# add_book(book): Adds a Book object to the library.
    def add_book(self, book):
        self.books.append(book)
        return f"Added {book.title} by {book.author}"
# show_available_books(): Prints all books where is_borrowed is False.