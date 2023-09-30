# Q 1: Write a program that takes a sentence as input and counts the number of words in it.

print("Takes a sentence as input and counts the number of words in it \n")

while (1):
    try:
        inputValue = input("Enter a sentence : ")
        wordList = inputValue.split()
        break
    except:
        print("Incorrect inputs! Try again")
        continue

print("Total number of words in given sentence is ", len(wordList))
