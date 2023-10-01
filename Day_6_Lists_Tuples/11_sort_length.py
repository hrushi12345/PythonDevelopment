# Q 11: Create a function that takes a list of strings and returns the list sorted by the length of the strings.

print("Takes a list of strings and returns the list sorted by the length of the strings \n")

global inputList

while (1):
    try:
        inputList = input("Enter elements seperated by comma : ")
        inputList = inputList.split(',')
        inputList = [item.strip() for item in inputList]
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def sortListByLength(inputList):
    for index in range(len(inputList)):
        for jndex in range(index, len(inputList)):
            if len(inputList[index]) > len(inputList[jndex]):
                temp = inputList[index]
                inputList[index] = inputList[jndex]
                inputList[jndex] = temp
    return inputList


print("Input list after sorting is ", sortListByLength(inputList))
