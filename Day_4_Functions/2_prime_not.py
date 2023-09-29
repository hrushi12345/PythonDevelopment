# Q 2: Create a function to check if a number is prime.

print("Check if a number is prime or not \n")

global inputValue

while (1):
    try:
        inputValue = int(input("Enter a number : "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def primeOrNot(inputValue):
    isPrime = True
    if inputValue != 2:
        for num in range(2, int(inputValue/2) + 1):
            if inputValue % num == 0:
                isPrime = False
    return isPrime


if primeOrNot(inputValue):
    print("Given number is Prime")
else:
    print("Given number is not Prime")
