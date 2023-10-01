# Q 10: Given two sets, find the union, intersection, and difference between them.

print("Find the union, intersection, and difference between them \n")

while (1):
    try:
        inputList = input("Enter numbers in set 1 seperated by comma : ")
        inputList = inputList.split(',')
        inputSet1 = set(inputList)
        inputList = input("Enter numbers in set 2 seperated by comma : ")
        inputList = inputList.split(',')
        inputSet2 = set(inputList)
        break
    except:
        print("Incorrect inputs! Try again")
        continue

# union

unionOfSets = inputSet1.union(inputSet2)

print("Union of set 1 and set 2 is ", unionOfSets)

# intersection

intersectionOfSets = inputSet1.intersection(inputSet2)

print("Intersection of set 1 and set 2 is ", intersectionOfSets)

# difference

differenceOfSets = inputSet1.difference(inputSet2)

print("Difference of set 1 and set 2 is ", differenceOfSets)
