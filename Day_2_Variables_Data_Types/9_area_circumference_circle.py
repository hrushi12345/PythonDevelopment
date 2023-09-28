# Q 9: Calculate the area and circumference of a circle given its radius.

import ast

print("Calculate area and circumferenec of circle : ")

while (1):
    try:
        radius = ast.literal_eval(input("Enter radius : "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue

pi = 3.14
area = pi * radius * radius
circumference = 2 * pi * radius

print("Area of circle is : ", area)
print("Circumference of circle is : ", circumference)
