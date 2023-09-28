# Q 3: Convert temperature from Celsius to Fahrenheit.
# fah = cel * 1.5 + 32
import ast
print("Celsius to Fahrenheit Conversion \n")

while (1):
    try:
        cel = ast.literal_eval(input("Enter temprature in Celcius: "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue

fah = cel * 1.5 + 32

print("Temprature in Fahrenheit after conversion is : ", fah)
