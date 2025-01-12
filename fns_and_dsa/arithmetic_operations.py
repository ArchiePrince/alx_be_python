# Title: Arithmetic Operation Function
# Author: Archie Prince
# Filename: daily_reminder.py
# Date: 22.12.2024
# Objective: A script to define a function that performs basic arithmetic operations. 
# This function, perform_operation, will be imported and used in a separate main.py script, provided.

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: The result of the operation, or a message in case of an error.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"