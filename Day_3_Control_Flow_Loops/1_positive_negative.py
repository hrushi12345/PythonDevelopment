# Q 1: Write a program that checks if a given number is positive, negative, or zero.

import ast

print("Checks if a given number is positive, negative, or zero : ")

while (1):
    try:
        inputNumber = ast.literal_eval(input("Enter a number : "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue
    
if inputNumber > 0:
    print("Given number is Positive.")
elif inputNumber < 0:
    print("Given number is Negative.")
else:
    print("Given number is Zero.")