# Q 3: Implement a function that reverses a given string.

print("Reverse a string \n")

global inputValue

while (1):
    try:
        inputValue = input("Enter a string : ")
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def reverseString(inputString):
    return inputString[::-1]


print("Reverse of input string is ", reverseString(inputValue))
