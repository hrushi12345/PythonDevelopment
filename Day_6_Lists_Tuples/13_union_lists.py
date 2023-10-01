# Q 13: Implement a function that takes two lists and returns their union (all unique elements from both lists).

print("Takes two lists and returns their union \n")

while (1):
    try:
        inputList1 = input("Enter list 1 elements seperated by comma : ")
        inputList1 = inputList1.split(',')
        inputList1 = [item.strip() for item in inputList1]
        inputList2 = input("Enter list 2 elements seperated by comma : ")
        inputList2 = inputList2.split(',')
        inputList2 = [item.strip() for item in inputList2]
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def union2Lists(inputList1, inputList2):
    return inputList1 + [item for item in inputList2 if item not in inputList1]


print("Union of 2 input list is ", union2Lists(inputList1, inputList2))
