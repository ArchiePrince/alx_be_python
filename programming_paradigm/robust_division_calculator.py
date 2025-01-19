# Title: Create a Simple Bank Account Class
# Author: Archie Prince
# Filename: robust_division_calculator.py
# Date: 19.01.2025
# Objective: Implement a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.

def safe_divide(numerator, denominator):
    """
    Performs division with error handling for division by zero and non-numeric inputs.

    :param numerator: The numerator for the division.
    :param denominator: The denominator for the division.
    :return: The result of the division or an appropriate error message.
    """
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform division
        result = numerator / denominator
        return f"Result: {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
