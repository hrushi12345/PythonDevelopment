# Q 11: Create a function to count the number of vowels in a given string.

print("Count number of vowels from string : ")

global inputString

while (1):
    try:
        inputString = input("Enter a string: ")
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def countVowels(string):
    vowelList = "aeiou"
    count = 0
    for char in string.lower():
        if char in vowelList:
            count += 1
    return count


if __name__ == "__main__":
    count = countVowels(inputString)

print("Total number of vowels in input string are ", count)
