# Q 6: Write a function to remove all duplicate characters from a given string.

print("Remove all duplicate characters from a given string \n")

global inputValue

while (1):
    try:
        inputValue = input("Enter a string : ")
        break
    except:
        print("Incorrect inputs! Try again")
        continue

usedCharactersList = []


def removeDuplicateChar(inputString):
    for char in inputString:
        if char in usedCharactersList:
            inputString = inputString.replace(char, '')
        else:
            usedCharactersList.append(char)
    inputString = ''.join(usedCharactersList)
    return inputString


print("Input string after removing duplicate characters is ",
      removeDuplicateChar(inputValue))
