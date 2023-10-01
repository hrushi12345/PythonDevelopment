# Q 10: Given a list of names, remove all duplicate names and print the unique names

print("Remove all duplicate names and print the unique names \n")

while (1):
    try:
        inputList = input("Enter elements seperated by comma : ")
        inputList = inputList.split(',')
        inputList = [item.strip() for item in inputList]
        break
    except:
        print("Incorrect inputs! Try again")
        continue

uniqueList = []
for item in inputList:
    if item not in uniqueList:
        uniqueList.append(item)

print("Input list after removing duplicates is ", uniqueList)
