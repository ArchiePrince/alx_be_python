# Title: Implementing Basic OOP for a Library Management System
# Author: Archie Prince
# Filename: library_management.py
# Date: 19.01.2025
# Objective: Solidify understanding of basic OOP concepts in Python by implementing a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.


class Book:
    """Represents a book with a title, author, and availability status."""

    def __init__(self, title, author):
        """
        Initialize the book with a title, author, and default availability.
        :param title: Title of the book.
        :param author: Author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns the availability status of the book."""
        return not self._is_checked_out


class Library:
    """Represents a library that manages a collection of books."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private list to store book instances

    def add_book(self, book):
        """
        Adds a book to the library's collection.
        :param book: Instance of the Book class to add.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book by its title.
        :param title: Title of the book to check out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                    return
        print(f"'{title}' is either not available or does not exist in the library.")

    def return_book(self, title):
        """
        Returns a book by its title.
        :param title: Title of the book to return.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"'{title}' has been returned.")
                    return
        print(f"'{title}' is either not checked out or does not exist in the library.")

    def list_available_books(self):
        """Lists all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
