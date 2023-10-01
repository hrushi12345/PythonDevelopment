# Q 3: Access elements in a tuple using indexing.

print("Access elements in a tuple using indexing \n")

while (1):
    try:
        inputList = input("Enter elements seperated by comma : ")
        tupleValues = tuple(inputList.split(','))
        break
    except:
        print("Incorrect inputs! Try again")
        continue

print("All elements from input tuple is ", tupleValues)

print("1st element from input tuple is ", tupleValues[0])

print("Last element from input tuple is ", tupleValues[-1])

print("2nd last element from input tuple is ", tupleValues[-2])
