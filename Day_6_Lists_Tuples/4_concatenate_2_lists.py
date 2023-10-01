# Q 4: Given two lists of numbers, concatenate them into a single list.

print("Concatenate 2 lists into a single list \n")

while (1):
    try:
        inputList1 = input("Enter input list 1 elements seperated by comma : ")
        inputList1 = inputList1.split(',')
        inputList2 = input("Enter input list 2 elements seperated by comma : ")
        inputList2 = inputList2.split(',')
        break
    except:
        print("Incorrect inputs! Try again")
        continue

inputList1.extend(inputList2)

print("Concatenated final list is ", inputList1)
