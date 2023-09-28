# Q 3: Create a list of fruits and access elements using indexing.

print("List of fruits and indexing : ")

while (1):
    try:
        inputString = input("Enter fruit names seperated by comma : ")
        fruitList = inputString.split(",")
        break
    except:
        print("Incorrect inputs! Try again")
        continue

print("Fruit list is : ", fruitList)
print("First fruit is : ", fruitList[0])
print("Last fruit is : ", fruitList[-1])
print("Second fruit is : ", fruitList[1])
print("Reverse fruit list is : ", fruitList[::-1])
