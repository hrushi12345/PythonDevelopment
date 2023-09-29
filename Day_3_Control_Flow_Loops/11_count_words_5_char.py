# Q 11: Given a list of words, count the number of words with more than five characters.

print("Count the number of words with more than five characters \n")

while (1):
    try:
        inputList = input("Enter a words seperated by comma : ")
        wordList = inputList.split()
        break
    except:
        print("Incorrect inputs! Try again")
        continue

count = 0
for word in wordList:
    if len(word) >= 5:
        count += 1

print("Number of words with more than five characters are ", count)
