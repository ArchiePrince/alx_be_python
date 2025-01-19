# Title: Create a Simple Bank Account Class
# Author: Archie Prince
# Filename: main.py
# Date: 19.01.2025
# Objective: Implement a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.


import sys
from robust_division_calculator import safe_divide

def main():
    """
    Command-line interface for the safe_divide function.
    Expects exactly two arguments: numerator and denominator.
    """
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the safe_divide function and display the result
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
