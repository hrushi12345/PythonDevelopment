# Q 3: Write a Python program to find the length of the longest word in a sentence.

print("Find the length of the longest word in a sentence \n")

while (1):
    try:
        inputValue = input("Enter a sentence : ")
        wordList = inputValue.split()
        break
    except:
        print("Incorrect inputs! Try again")
        continue

maxWordLength = 0
for word in wordList:
    if len(word) > maxWordLength:
        maxWordLength = len(word)

print("Length of longest word in given sentence is ", maxWordLength)
