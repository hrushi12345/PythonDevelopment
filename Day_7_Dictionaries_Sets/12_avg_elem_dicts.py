# Q 12: Write a program that finds the average value of all the elements in a list of dictionaries.

print("Finds the average value of all the elements in a list of dictionaries \n")

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
        break
    except:
        print("Incorrect inputs! Try again")
        continue

totalCount = 0
sum1 = 0
for items in finalInputList:
    totalCount += len(items.values())
    print(items.values())
    sum1 += sum(items.values())

print("Average value of all the elements in a list of dictionaries is ",sum1/totalCount)
