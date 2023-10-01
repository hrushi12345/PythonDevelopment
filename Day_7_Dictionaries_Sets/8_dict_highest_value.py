# Q 8: Given a list of dictionaries, find the dictionary with the highest value for a specific key.

print("Find the dictionary with the highest value for a specific key \n")

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
        specificKey = input("Enter common key for all the dictionaries ")
        break
    except:
        print("Incorrect inputs! Try again")
        continue

maxValueDictIndex = 0
for index, value in enumerate(finalInputList):
    if value[specificKey] > finalInputList[maxValueDictIndex][specificKey]:
        maxValueDictIndex = index

print("Dictionary with max value of key " + specificKey +
      " is " + str(finalInputList[maxValueDictIndex]))
