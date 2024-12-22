# Title: Match Case Calculator for Arithmetic Operations
# Author: Archie Prince
# Filename: match_case_calculator.py

print("Match Case Calculator for Arithmetic Operations!!!\n")

#Prompt user to enter first number
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input('Choose the operation (+, -, *, /): ')

match operation:
    case '+':
        result = num1 + num2
        print(f'The result is {result}.')
    case '-':
        result = num2 - num1
        print(f'The result is {result}.')
    case '*':
        result = num1 * num2
        print(f'The result is {result}.')
    case '/':
        if num2 == 0:
            print('Cannot divide by zero.')
            
        else:
            result = num1 / num2 
            print(f'The result is {result}')


        