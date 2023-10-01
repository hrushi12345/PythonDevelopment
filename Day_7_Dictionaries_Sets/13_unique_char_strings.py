# Q 13: Implement a function that takes a list of strings and returns a set of unique characters present in all strings

print("Takes a list of strings and returns a set of unique characters present in all strings \n")

print("Set of unique characters present in all strings \n")

while (1):
    try:
        inputList = input("Enter strings seperated by comma : ")
        stringList = inputList.split(',')
        stringList = [value.strip() for value in stringList]
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def uniqueCharacters(string):
    return set(string)


print("Unique characters present in input strings are ")
for string in stringList:
    print(uniqueCharacters(string))
