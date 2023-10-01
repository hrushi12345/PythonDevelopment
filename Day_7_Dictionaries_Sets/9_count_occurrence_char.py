# Q 9: Write a Python program that counts the number of occurrences of each character in a given string using a dictionary

print("Counts the number of occurrences of each character in a given string using a dictionary \n")

while (1):
    try:
        inputString = input("Enter a string : ")
        break
    except:
        print("Incorrect inputs! Try again")
        continue

uniqueDict = {}
for char in inputString:
    if char not in uniqueDict.keys():
        uniqueDict[char] = 1
    else:
        uniqueDict[char] += 1
        
print("Number of occurence of each character in given sequence is ",uniqueDict)