# Q 4: Given two dictionaries, merge them into a single dictionary.

print("Merge 2 dictionary into a single dictionary \n")

while (1):
    try:
        inputList = input("Enter keys:value of dict 1 seperated by comma : ")
        inputList = inputList.split(',')
        inputDict1 = {}
        for item in inputList:
            inputDict1[item.split(":")[0]] = item.split(":")[1]
        inputList = input("Enter keys:value of dict 2 seperated by comma : ")
        inputList = inputList.split(',')
        inputDict2 = {}
        for item in inputList:
            inputDict2[item.split(":")[0]] = item.split(":")[1]
        break
    except:
        print("Incorrect inputs! Try again")
        continue

inputDict1.update(inputDict2)

newdictionary = inputDict1

print("New dictionary after merging 2 input dictionaries is ", newdictionary)
