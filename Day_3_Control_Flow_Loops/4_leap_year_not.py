# Q 4: Create a program that takes a year as input and checks if it is a leap year or not.

import ast

print("Checks if it is a leap year or not \n")

while (1):
    try:
        inputValue = ast.literal_eval(input("Enter a number : "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue

if inputValue % 4 == 0:
    print("Input value is leap year.")
else:
    print("Input value is not leap year.")
