# Title:  Distinguishing Between Class Methods and Static Methods
# Author: Archie Prince
# Filename: polymorphism_demo.py
# Date: 10.02.2025
# Objective: Solidify your understanding of class methods and static methods in Python by implementing examples of each in a class, demonstrating their usage and differences.



class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Returns the product of two numbers and prints the calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b