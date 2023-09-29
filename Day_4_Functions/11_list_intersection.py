# Q 11: Write a function that takes two lists and returns their intersection (common elements).

print("Takes two lists and returns their intersection (common elements) \n")

global inputList1, inputList2

while (1):
    try:
        inputList1 = input("Enter list 1 items seperated by comma : ")
        stringList1 = inputList1.split(",")
        strippedStringList1 = [val.strip() for val in stringList1]
        inputList2 = input("Enter list 2 items seperated by comma : ")
        stringList2 = inputList2.split(",")
        strippedStringList2 = [val.strip() for val in stringList2]
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def intersectionListDef(inputList1, inputList2):
    intersectionList = []
    for item in inputList1:
        if item in inputList2:
            intersectionList.append(item)
    return intersectionList


print("Intersection items from both input lists is ",
      intersectionListDef(strippedStringList1, strippedStringList2))
