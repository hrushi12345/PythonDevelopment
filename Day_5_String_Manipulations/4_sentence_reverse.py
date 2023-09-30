# Q 4: Create a function that takes a sentence as input and returns the sentence in reverse order.

print("Takes a sentence as input and returns the sentence in reverse order \n")

global inputValue

while (1):
    try:
        inputValue = input("Enter a sentence : ")
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def reverseSentence(inputString):
    return inputString[::-1]


print("Reverse of the input sentence is ", reverseSentence(inputValue))
