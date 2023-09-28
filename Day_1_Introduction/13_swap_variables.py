# Q 13: Implement a program that swaps the values of two variables.

# print("Swap the values of 2 variables \n")

while (1):
    try:
        inputVal1 = input("Enter 1st value: ")
        inputVal2 = input("Enter 2nd value: ")
        break
    except:
        print("Incorrect inputs! Try again")
        continue

temp = inputVal1
inputVal1 = inputVal2
inputVal2 = temp

print("After swap - 1st value is " + inputVal1 + " & 2nd value is " + inputVal2)
