# Q 7: Given a list of names, concatenate them into a single string separated by spaces.

print("Concatenate multiple strings into single : ")

while (1):
    try:
        inputList = input("Enter string list seperated by spaces : ")
        stringList = inputList.split()
        break
    except:
        print("Incorrect inputs! Try again")
        continue

singleString = ""
for string in stringList:
    singleString += string

print("Single string after concatenating multiple strings : ",singleString)