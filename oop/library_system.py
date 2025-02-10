# Title:  Mastering Inheritance and Composition in Python
# Author: Archie Prince
# Filename: library_system.py
# Date: 10.02.2025
# Objective: Deepen your understanding of inheritance and composition in Python by creating a system that models a library with different types of books.


class Book:
    def __init__(self, title: str, author: str):
        """Initializes a Book instance with title and author."""
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Initializes an EBook instance with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Initializes a PrintBook instance with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        """Initializes a Library instance with an empty book collection."""
        self.books = []
    
    def add_book(self, book: Book):
        """Adds a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)
    
    def list_books(self):
        """Prints details of each book in the library."""
        for book in self.books:
            print(book)

