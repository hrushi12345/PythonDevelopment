# Q 7: Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence.

print("Checks if the word is present in the sentence \n")

while (1):
    try:
        inputSentence = input("Enter a sentence : ")
        inputWord = input("Enter a word : ")
        break
    except:
        print("Incorrect inputs! Try again")
        continue

if inputWord in inputSentence:
    print("Input word is present in sentence.")
else:
    print("Input word is not present in sentence.")
