# Q 7: Given a list of names, print all names starting with the letter 'A'.

print("Print all names starting with the letter 'A' \n")

while (1):
    try:
        inputList = input("Enter names seperated ny comma : ")
        nameList = inputList.split(",")
        break
    except:
        print("Incorrect inputs! Try again")
        continue

nameListStartWithA = []
for name in nameList:
    if name.strip()[0].lower() == 'a':
        nameListStartWithA.append(name)

print("List starting with letter A are ", nameListStartWithA)
