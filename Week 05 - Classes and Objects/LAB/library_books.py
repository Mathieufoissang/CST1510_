"""Library Books

Create a Book with title, author, and is_available (default True), plus
borrow() and return_book() methods. Store 4 books in a list; borrow one and
try it a second time (printing a message), print all available books, then ask
the user for an author and print all books by that author.
"""


class Book:
    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f'You borrowed "{self.title}".')
            return True
        print(f'"{self.title}" is already borrowed.')
        return False

    def return_book(self):
        if self.is_available:
            print(f'"{self.title}" is already available.')
        else:
            self.is_available = True
            print(f'You returned "{self.title}".')


books = [
    Book("Pride and Prejudice", "Jane Austen"),
    Book("Emma", "Jane Austen"),
    Book("1984", "George Orwell"),
    Book("The Hobbit", "J. R. R. Tolkien"),
]

books[0].borrow()
books[0].borrow()  # The second attempt reports that it is already borrowed.

print("\nAvailable books:")
for book in books:
    if book.is_available:
        print(f"- {book.title} by {book.author}")

try:
    requested_author = input("\nEnter an author to search for: ").strip()
except EOFError:
    # Keep the script usable in environments that run it without interactive input.
    requested_author = ""

if requested_author:
    matching_books = [
        book for book in books if book.author.casefold() == requested_author.casefold()
    ]
    if matching_books:
        print(f"Books by {requested_author}:")
        for book in matching_books:
            print(f"- {book.title}")
    else:
        print(f"No books found by {requested_author}.")
else:
    print("No author entered; skipping the author search.")
