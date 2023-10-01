# Q 11: Create a function that takes a list of dictionaries and sorts them based on a specified key.

print("Takes a list of dictionaries and sorts them based on a specified key \n")

while (1):
    try:
        inputList = input("Enter keys:value of dict 1 seperated by comma : ")
        inputList = inputList.split(',')
        inputDict1 = {}
        for item in inputList:
            inputDict1[item.split(":")[0]] = int(item.split(":")[1])
        inputList = input("Enter keys:value of dict 2 seperated by comma : ")
        inputList = inputList.split(',')
        inputDict2 = {}
        for item in inputList:
            inputDict2[item.split(":")[0]] = int(item.split(":")[1])
        inputList = input("Enter keys:value of dict 3 seperated by comma : ")
        inputList = inputList.split(',')
        inputDict3 = {}
        for item in inputList:
            inputDict3[item.split(":")[0]] = int(item.split(":")[1])
        finalInputList = [inputDict1, inputDict2, inputDict3]
        specificKey = input("Enter common key for all the dictionaries : ")
        break
    except:
        print("Incorrect inputs! Try again")
        continue

for index, value in enumerate(finalInputList):
    for jndex in range(index, len(finalInputList)):
        if finalInputList[index][specificKey] > finalInputList[jndex][specificKey]:
            temp = finalInputList[jndex]
            finalInputList[jndex] = finalInputList[index]
            finalInputList[index] = temp

print("Sorted input dictiory list by key " +
      specificKey+" is "+str(finalInputList))
