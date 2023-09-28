# Q 11: Given a list of integers, find the sum of all positive numbers.

print("Sum of all positive numbers \n")

while (1):
    try:
        inputList = input("Enter integers seperated by comma: ")
        numberList = inputList.split(",")
        intList = [int(number) for number in numberList]
        break
    except:
        print("Incorrect inputs! Try again")
        continue

sum = 0
for integer in intList:
    if integer > 0:
        sum += integer

print("Sum of all positive integers is : ", sum)
