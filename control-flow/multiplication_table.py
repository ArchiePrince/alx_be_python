# Title: Multiplication Table for a given number
# Author: Archie Prince
# Filename: multiplication_table.py
#  Objective: Use a for loop to generate and print the multiplication table for a given number.

print('Multiplication Table!\n')

#Prompt user for a number to see its multiplication table
quotient = int(input('Enter a number to see its multiplication table: '))

#Print the times table from 1-10
for i in range(1, 11):
    product = quotient * i
    print(f"{quotient} x {i} = {product}")