# Q 7: Create a program that finds the common elements between two lists and stores them in a new list.

print("Finds the common elements between two lists and stores them in a new list \n")

while (1):
    try:
        inputList1 = input("Enter input list 1 seperated by comma : ")
        inputList1 = inputList1.split(',')
        inputList2 = input("Enter input list 2 seperated by comma : ")
        inputList2 = inputList2.split(',')
        break
    except:
        print("Incorrect inputs! Try again")
        continue


commonList = [value for value in inputList1 if value in inputList2]

print("Common list from both input lists is ", commonList)
