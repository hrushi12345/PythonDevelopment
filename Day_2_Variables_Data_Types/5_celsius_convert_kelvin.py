# Q 5: Create a program that takes a temperature in Celsius and
# converts it to Kelvin.
# Kelvin = Celsius + 273.15

import ast

print("Convert temperature from Celsius to Kelvin : ")

while (1):
    try:
        temp = ast.literal_eval(input("Enter temperature in celsius : "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue

kelvin = temp + 273.15

print("Temperature in kelvin after conversion is : ", kelvin)
