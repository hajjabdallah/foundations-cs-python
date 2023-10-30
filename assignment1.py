# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:58:07 2023

@author: Abdal
"""
# EX1
# Get input from the user
top = float(input("Enter the top value: "))
bottom = float(input("Enter the bottom value: "))
val = float(input("Enter the value to check: "))

# Check if val is between top and bottom
is_between = bottom <= val <= top

# Print the result
print(is_between)


# EX2


# Get input from the user
a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))
c = int(input("Enter the third integer (c): "))

# Find the maximum and minimum values
maximum = max(a, b, c)
minimum = min(a, b, c)

# Print the results
print(f"The maximum value is {maximum}")
print(f"The minimum value is {minimum}")


# EX3

# Get input from the user
total_grade = float(input("Enter your total grade: "))

# Determine the letter grade
if total_grade > 89:
    letter_grade = "A"
elif total_grade > 79:
    letter_grade = "B"
elif total_grade > 69:
    letter_grade = "C"
elif total_grade > 59:
    letter_grade = "D"
else:
    letter_grade = "F"

# Print the letter grade
print(f"Your letter grade is {letter_grade}")


