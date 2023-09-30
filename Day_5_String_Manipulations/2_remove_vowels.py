# Q 2: Given a string, write a function to remove all vowels from it and return the modified string.

print("Remove all vowels from it and return the modified string \n")

global inputValue

while (1):
    try:
        inputValue = input("Enter a string : ")
        wordList = inputValue.split()
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def removeVowels(inputValue):
    return inputValue.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')


print("Modified string after removing all the vowels", removeVowels(inputValue))
