# Q 6: Implement a function that returns the factorial of a given number using recursion.

print("Calculates the factorial of a given number using recursion \n")

global inputValue

while (1):
    try:
        inputValue = int(input("Enter a number : "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def factorialNumber(number, fact):
    if number == 1:
        return fact
    else:
        fact *= number
        number -= 1
        return factorialNumber(number, fact)


print("Factorial of a input number is ", factorialNumber(inputValue, 1))
