# Q 6: Implement a function that takes a list of numbers and returns a new list with the squared values

import ast

print("Takes a list of numbers and returns a new list with the squared values \n")

global numberList

while (1):
    try:
        inputList = input("Enter numbers seperated by comma : ")
        numberList = inputList.split(',')
        numberList = [ast.literal_eval(number) for number in numberList]
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def squareList(numberList):
    return [number*number for number in numberList]


print("Print square of input list is ", squareList(numberList))
