# Q 5: Write a program that finds the largest and smallest elements in a list.

import ast

print("Finds the largest and smallest elements in a list \n")

while (1):
    try:
        inputList = input("Enter numbers seperated by comma : ")
        numberList = inputList.split(',')
        numberList = [ast.literal_eval(number) for number in numberList]
        break
    except:
        print("Incorrect inputs! Try again")
        continue

largestNumber = max(numberList)
smallestNumber = min(numberList)

print("Largest number from input list is ", largestNumber)
print("Smallest number from input list is ", smallestNumber)
