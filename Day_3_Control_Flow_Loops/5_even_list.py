# Q 5: Given a list of integers, find all the even numbers and store them in a new list.

print("Find all the even numbers and store them in a new list \n")

while (1):
    try:
        inputList = input("Enter numbers seperated ny comma : ")
        numberList = inputList.split(",")
        numberList = [int(number) for number in numberList]
        break
    except:
        print("Incorrect inputs! Try again")
        continue

evenList = []
for number in numberList:
    if number % 2 == 0:
        evenList.append(number)

print("Even number list is ", evenList)
