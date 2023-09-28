# Q 4: Given a list of numbers, find the sum and average.

print("Sum and average of numbers : ")

while (1):
    try:
        inputList = input("Enter numbers seperated ny comma : ")
        numberList = inputList.split(",")
        numberList = [eval(number) for number in numberList]
        count = len(numberList)
        break
    except:
        print("Incorrect inputs! Try again")
        continue
sum = 0
for number in numberList:
    sum += number
    
print("Sum of all numbers is : ",sum)
print("Average of all numbers is : ",sum/count)
