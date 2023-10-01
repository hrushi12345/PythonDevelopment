# Q 6: Implement a function that removes a key-value pair from a dictionary.

print("Removes a key-value pair from a dictionary \n")

while (1):
    try:
        inputList = input("Enter keys:value of dict seperated by comma : ")
        inputList = inputList.split(',')
        inputDict = {}
        for item in inputList:
            inputDict[item.split(":")[0]] = item.split(":")[1]
        stringValue = input("Enter keys:value to be removed : ")
        keyValuePair = {stringValue.split(':')[0]: stringValue.split(':')[1]}
        break
    except:
        print("Incorrect inputs! Try again")
        continue

del inputDict[list(keyValuePair.keys())[0]]

print("Input dict after removing a key-value pair ", inputDict)
