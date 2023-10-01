# Q 1: Given a list of numbers, find the sum and average using built-in functions.

import ast

print("Find the sum and average using built-in functions \n")

while (1):
    try:
        inputList = input("Enter numbers seperated by comma : ")
        numberList = inputList.split(',')
        numberList = [ast.literal_eval(number) for number in numberList]
        break
    except:
        print("Incorrect inputs! Try again")
        continue

sumOfNumbers = sum(numberList)
averageOfNumbers = sumOfNumbers/len(numberList)

print("Sum of input numbers is " + str(sumOfNumbers))
print("Average of input numbers is " + str(averageOfNumbers))
