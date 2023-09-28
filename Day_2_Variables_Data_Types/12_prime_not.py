# Q 12: Write a program to check if a number is prime.

print("Check if a number is prime : ")

while (1):
    try:
        inputNumber = int(input("Enter a number : "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue

if inputNumber == 2:
    isPrime = True
else:
    isPrime = True
    for num in range(2, inputNumber):
        if inputNumber % num == 0:
            isPrime = False
            break

if isPrime:
    print("Number is prime.")
else:
    print("Number is not prime.")
