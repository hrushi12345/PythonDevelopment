# Q 12: Write a program that checks if a given list is sorted in ascending order

import ast

print("Checks if a given list is sorted in ascending order \n")

while (1):
    try:
        inputList = input("Enter numbers seperated by comma : ")
        inputList = inputList.split(',')
        inputList = [ast.literal_eval(item) for item in inputList]
        break
    except:
        print("Incorrect inputs! Try again")
        continue

inputListCopy = inputList.copy()

for index in range(len(inputList)):
    for jndex in range(index, len(inputList)):
        if inputList[index] > inputList[jndex]:
            temp = inputList[index]
            inputList[index] = inputList[jndex]
            inputList[jndex] = temp


if inputList == inputListCopy:
    print("Input list is in ascending order")
else:
    print("Input list is not in ascending order")
