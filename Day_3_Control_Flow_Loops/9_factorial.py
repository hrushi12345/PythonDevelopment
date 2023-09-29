# Q 9: Write a program that calculates the factorial of a given number.

print("Calculates the factorial of a given number \n")

while (1):
    try:
        inputValue = int(input("Enter a number : "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue

fact = 1
for i in range(1, inputValue+1):
    fact *= i

print("Factorial of a number is ", fact)
