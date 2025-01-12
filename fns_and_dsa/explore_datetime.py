# Title: Explore `datetime` Module
# Author: Archie Prince
# Filename: explore_datetime.py
# Date: 12.01.2025
# Objective: Familiarize yourself with Python’s datetime module by writing a script that performs specified operations with dates and times.

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in the format "YYYY-MM-DD HH:MM:SS".
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Calculate a future date based on user input and print it in the format "YYYY-MM-DD".
    """
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=number_of_days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter an integer value.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()