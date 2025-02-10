# Title:  Exploring Polymorphism and Method Overriding
# Author: Archie Prince
# Filename: polymorphism_demo.py
# Date: 10.02.2025
# Objective: Enhance your understanding of polymorphism in Python by creating a set of classes that demonstrate method overriding and polymorphic behavior.


import math

class Shape:
    def area(self):
        """Raises an error if not implemented in a derived class."""
        raise NotImplementedError("Subclasses must override the area method.")

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        """Initializes a Rectangle instance with length and width."""
        self.length = length
        self.width = width
    
    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius: float):
        """Initializes a Circle instance with radius."""
        self.radius = radius
    
    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * self.radius ** 2