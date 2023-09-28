# Q 12: Create a program that takes a sentence as input and 
# counts the number of words in it.

print("Count number of words from sentence \n")

while (1):
    try:
        inputString = input("Enter sentence: ")
        count = len(inputString.split())
        break
    except:
        print("Incorrect inputs! Try again")
        continue
    
print("Number of words in sentence are ", str(count))
