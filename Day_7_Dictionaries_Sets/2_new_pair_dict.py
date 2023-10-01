# Q 2: Add a new key-value pair to an existing dictionary

import ast

print("Add a new key-value pair to an existing dictionary \n")

while (1):
    try:
        inputList = input("Enter keys:value of dict seperated by comma : ")
        inputList = inputList.split(',')
        inputDict1 = {}
        for item in inputList:
            inputDict1[item.split(":")[0]] = item.split(":")[1]
        inputString = input("Enter new key:value to add in dict : ")
        inputDict2 = {inputString.split(":")[0]: inputString.split(":")[1]}
        break
    except:
        print("Incorrect inputs! Try again")
        continue


inputDict1[list(inputDict2.keys())[0]] = inputDict2[list(inputDict2.keys())[0]]

print("Input dict after adding new key-value is ", inputDict1)
