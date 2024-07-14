class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def is_checked_out(self):
        return self._is_checked_out

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Expected an instance of Book")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.is_checked_out():
                    book.check_out()
                else:
                    print(f"'{title}' is already checked out.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.is_checked_out():
                    book.return_book()
                else:
                    print(f"'{title}' is not checked out.")

    def list_available_books(self):
        available_books = [book for book in self._books if not book.is_checked_out()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books.")