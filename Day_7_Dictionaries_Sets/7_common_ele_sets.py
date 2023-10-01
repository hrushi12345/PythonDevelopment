# Q 7: Create a program that checks if two sets have any elements in common.

print("Checks if two sets have any elements in common \n")

while (1):
    try:
        inputList1 = input("Enter elements of set 1 seperated by comma : ")
        inputSet1 = set(inputList1.split(','))
        inputList2 = input("Enter elements of set 2 seperated by comma : ")
        inputSet2 = set(inputList2.split(','))
        break
    except:
        print("Incorrect inputs! Try again")
        continue

isCommonElement = False
for item in inputSet1:
    if item in inputSet2:
        isCommonElement = True
        break

if isCommonElement:
    print("Both input sets have common element.")
else:
    print("Both input sets have no common element.")
