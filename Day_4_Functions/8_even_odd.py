# Q 8: Write a function to check if a number is even or odd and return "Even" or "Odd" accordingly.

print('''Check if a number is even or odd and return "Even" or "Odd" accordingly \n''')

global inputValue

while (1):
    try:
        inputValue = int(input("Enter a number : "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def even_Odd(inputValue):
    if inputValue % 2 == 0:
        return "Even"
    else:
        return "Odd"


print("Given number is ", even_Odd(inputValue))
