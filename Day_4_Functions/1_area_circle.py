# Q 1: Write a function to calculate the area of a circle given its radius.

import ast

print("Calculates the factorial of a given number \n")

global radius

while (1):
    try:
        radius = ast.literal_eval(input("Enter a radius : "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def areaOfCircle(radius):
    pi = 3.14
    return pi * radius * radius


print("Area of circle is ", areaOfCircle(radius))
