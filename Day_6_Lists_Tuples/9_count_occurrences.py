# Q 9: Write a Python program to count the occurrences of each element in a given list.

print("Count the occurrences of each element in a given list \n")

while (1):
    try:
        inputList = input("Enter elements seperated by comma : ")
        inputList = inputList.split(',')
        inputList = [item.strip() for item in inputList]
        break
    except:
        print("Incorrect inputs! Try again")
        continue


uniqueList = list(set(inputList))


def countOccurrence(item, inputList):
    count = 0
    for i in inputList:
        if i == item:
            count += 1
    return count


occurrencesDict = {}
for item in uniqueList:
    occurrencesDict[item] = countOccurrence(item, inputList)

print("Count of occurrences of each element is ", occurrencesDict)
