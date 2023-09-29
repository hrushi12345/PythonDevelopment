# Q 3: Implement a program that finds the largest number in a list.

import ast

print("Finds the largest number in a list \n")

while (1):
    try:
        inputList = input("Enter numbers seperated ny comma : ")
        numberList = inputList.split(",")
        numberList = [ast.literal_eval(number) for number in numberList]
        break
    except:
        print("Incorrect inputs! Try again")
        continue
    
maxNo = numberList[0]
for number in numberList:
    if maxNo < number:
        maxNo = number

print("Largest number from list is ",maxNo)