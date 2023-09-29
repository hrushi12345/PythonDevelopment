# Q 7: Create a function to find the square of each element in a given list.

print("Find the square of each element in a given list \n")

global numberList

while (1):
    try:
        inputValue = input("Enter numbers seperated by comma : ")
        numberList = inputValue.split(",")
        numberList = [int(number) for number in numberList]
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def squareAllElements(numberList):
    for number in numberList:
        print(number*number)


print("Squares of all the elements in input list is ")
squareAllElements(numberList)
