# Q 5: Given a list of names, count the number of names that start with a vowel.

print("Count the number of names that start with a vowel \n")

while (1):
    try:
        inputValue = input("Enter a sentence : ")
        wordList = inputValue.split()
        break
    except:
        print("Incorrect inputs! Try again")
        continue

count = 0
for word in wordList:
    if word[0] in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print("Number of names start with vowel are ", count)
