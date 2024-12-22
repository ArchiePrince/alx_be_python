# Title: Drawing Patterns with Nested Loops
# Author: Archie Prince
# Filename: pattern_drawing.py
# Date: 22.12.2024
# Objective: Utilize while loops and nested for loops to draw a simple text-based pattern.


print('Draw Patterns with Nested Loops!\n')

#Prompt user for pattern size / length of square
length = int(input('Enter the size of the pattern: '))
i = 0

while i < length:

    for j in range(1, length + 1):
        print("*", end="")
    i += 1
    print()