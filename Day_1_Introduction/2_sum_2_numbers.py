# Q 2: Calculate the sum of two numbers entered by the user.
import ast
print("Sum of 2 numbers \n")
while (1):
    try:
        a = ast.literal_eval(input("Enter 1st number: "))
        b = ast.literal_eval(input("Enter 2nd number: "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue

sum = a + b
print("Sum of " + str(a) + " & " + str(b) + " is: ", sum)
