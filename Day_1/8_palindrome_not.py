# Q 8: Create a Python function to check if a given string is a palindrome.

print("Check string is Palindrome or not \n")

while (1):
    try:
        inputString = input("Enter string : ")
        reverseString = inputString[::-1]
        # print(reverseString)
        break
    except:
        print("Incorrect inputs! Try again")
        continue

if inputString == reverseString:
    print("String is Palindrome")
else:
    print("String is not Palindrome")
