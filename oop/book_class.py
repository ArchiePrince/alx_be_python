# Title:  Dive into Python Magic Methods
# Author: Archie Prince
# Filename: book_class.py
# Date: 10.02.2025
# Objective: Master Python magic methods by implementing a Book class that incorporates constructors (__init__), destructors (__del__), and the representation methods (__str__ and __repr__).

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Initializes a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """Destructor that prints a message when the book instance is deleted."""
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """Returns a human-readable string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Returns an official string representation for recreating the book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

