# Q 2: Create a list of fruits and add a new fruit to the list.

print("Add a new fruit to the list \n")

while (1):
    try:
        inputList = input("Enter fruits seperated by comma : ")
        fruitList = inputList.split(',')
        fruitList = [fruit.strip() for fruit in fruitList]
        fruitName = input("Enter fruit name: ")
        break
    except:
        print("Incorrect inputs! Try again")
        continue

print("Input fruit list ", fruitList)

fruitList.append(fruitName)
# fruitListAtEnd = fruitList.extend([fruitName])

print("Fruit list after adding new fruit at end of input list ", fruitList)

fruitList.insert(0, fruitName)

print("Fruit list after adding new fruit at start of input list ", fruitList)
