# Q 7: Given a list of numbers, find the maximum and minimum values.

import ast

print("Find maximum and minimum from List \n")

while (1):
    try:
        inputList = input("Enter numbers seperated by comma: ")
        numberList = inputList.split(',')
        numberList = [int(i) for i in numberList]
        max = min = numberList[0]
        for number in numberList:
            max = number if number >= max else max
            min = number if number <= min else min
        break
    except:
        print("Incorrect inputs! Try again")
        continue

print("Maximum number is : " + str(max) + "\nMinimum number is : " + str(min))
