# Q 4: Write a Python program to calculate the area of a
# rectangle given its length and width.

import ast

print("Calculate area of rectangle \n")
while (1):
    try:
        length = ast.literal_eval(input("Enter length of rectangle: "))
        breadth = ast.literal_eval(input("Enter breadth of rectangle: "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue

area = length * breadth

print("Area of rectangle is ", area)
