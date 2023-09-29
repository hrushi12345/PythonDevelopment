# Q 4: Given a list of numbers, create a function to find the sum of all positive numbers.

print("Find the sum of all positive numbers \n")

global numberList

while (1):
    try:
        inputList = input("Enter numbers seperated by comma : ")
        numberList = inputList.split(",")
        numberList = [int(number) for number in numberList]
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def sumPositiveNumbers(numberList):
    sum = 0
    for number in numberList:
        if number > 0:
            sum += number
    return sum


print("Sum of all positive numbsers is ", sumPositiveNumbers(numberList))
