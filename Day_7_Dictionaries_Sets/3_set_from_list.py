# Q 3: Create a set of unique numbers from a list of numbers

import ast

print("Create a set of unique numbers from a list of numbers \n")

while (1):
    try:
        inputList = input("Enter numbers seperated by comma : ")
        inputList = inputList.split(',')
        inputList = [ast.literal_eval(item) for item in inputList]
        break
    except:
        print("Incorrect inputs! Try again")
        continue

print("Input list is ", inputList)
uniqueItems = set(inputList)

print("Set created by input list is ", uniqueItems)
