# Q 6: Create a function to reverse a given string.

print("Function to reverse a string : ")

global inputString

while (1):
    try:
        inputString = input("Enter string : ")
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def reverseString(string):
    return string[::-1]


if __name__=="__main__":
    print("Reverse string of input string is :", reverseString(inputString))
