# Q 5: Create a program that takes a user's name and age as 
# input and prints a greeting message.

import ast

print("Greeting message \n")
while (1):
    try:
        name = input("Enter user's name: ")
        age = ast.literal_eval(input("Enter age of user: "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue

print("Hi, my name is " + name + ", and I am " + str(age) + " years old.")
