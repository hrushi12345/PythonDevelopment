# Q 5: Write a Python function to check if a given string is a palindrome.

print("Check if a given string is a palindrome \n")

global inputValue

while (1):
    try:
        inputValue = input("Enter a string : ")
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def isPalindrome(inputValue):
    reverseString = inputValue[::-1]
    if inputValue == reverseString:
        return True
    else:
        return False


if isPalindrome(inputValue):
    print("Given string is a Palindrome")
else:
    print("Given string is not a Palindrome")
