# Q 8: Given a list of words, find the word with the maximum length and its length.

print("Find the word with the maximum length and its length \n")

while (1):
    try:
        inputList = input("Enter words seperated by comma : ")
        wordList = inputList.split(',')
        break
    except:
        print("Incorrect inputs! Try again")
        continue

maxLengthWord = ''
for word in wordList:
    if len(word) > len(maxLengthWord):
        maxLengthWord = word

print("Word with maximum length is " + maxLengthWord +
      " & its length is " + str(len(maxLengthWord)))
