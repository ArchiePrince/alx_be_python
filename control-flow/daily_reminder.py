# Title: Personal Daily Reminder
# Author: Archie Prince
# Filename: daily_reminder.py
# Date: 22.12.2024
# Objective: Create a simplified Python script that uses conditional statements, Match Case, and loops 
# to remind the user about a single, priority task for the day based on time sensitivity.


while True:
    # Prompt user for task details
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Create the base reminder message
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")
            continue

    # Modify the message based on time sensitivity
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder += ". Consider completing it when you have free time."
    else:
        print("Invalid input for time-bound. Please enter yes or no.")
        continue

    # Print the customized reminder
    print(f"Reminder: {reminder}")

    # Check if the user wants to enter another task
    another = input("Do you want to enter another task? (yes/no): ").strip().lower()
    if another != "yes":
        break