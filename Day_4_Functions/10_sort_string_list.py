# Q 10: Create a function that takes a list of strings and returns the list sorted alphabetically

print("Takes a list of strings and returns the list sorted alphabetically \n")

global strippedStringList

while (1):
    try:
        inputList = input("Enter strings seperated by comma : ")
        stringList = inputList.split(",")
        strippedStringList = [string.strip() for string in stringList]
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def sortListString(stringList):
    stringList.sort()
    return stringList


print("Sorted list of strings is ", sortListString(strippedStringList))
