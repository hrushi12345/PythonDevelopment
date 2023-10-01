# Q 5: Write a program that finds the most frequent element in a list

print("Finds the most frequent element in a list \n")

while (1):
    try:
        inputList = input("Enter numbers seperated by comma : ")
        inputList = inputList.split(',')
        inputList = [item.strip() for item in inputList]
        break
    except:
        print("Incorrect inputs! Try again")
        continue

mostFrequentElement = max(set(inputList), key=inputList.count)

# largestElement = max(set(inputList))

print("Most frequent element from input list is ", mostFrequentElement)
