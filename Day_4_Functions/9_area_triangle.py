# Q 9: Calculate the area of a triangle given its base and height using a function.

import ast

print("Calculate the area of a triangle given its base and height \n")

global base, height

while (1):
    try:
        base = ast.literal_eval(input("Enter base of triangle : "))
        height = ast.literal_eval(input("Enter height of triangle : "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def areaTriangle(base, height):
    return base * height * 0.5


print("Area of triangle is ", areaTriangle(base, height))
