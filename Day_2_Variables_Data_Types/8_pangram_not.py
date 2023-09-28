# Q 8: Write a Python program to check if a given string is a pangram
# (contains all letters of the alphabet).

print("Check input text contains all letters of the alphabets : ")

while (1):
    try:
        inputString = input("Enter string : ")
        break
    except:
        print("Incorrect inputs! Try again")
        continue

alphabetList = 'abcdefghijklmnopqrstuvwxyz'
isPangram = True
for char in alphabetList:
    if char not in inputString.lower():
        isPangram = False

if isPangram:
    print("String is pangram.")
else:
    print("String is not pangram.")
