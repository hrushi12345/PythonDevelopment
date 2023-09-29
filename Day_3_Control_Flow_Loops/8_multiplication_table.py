# Q 8: Implement a program that prints the multiplication table of a given number.

print("Prints the multiplication table of a given number \n")

while (1):
    try:
        inputValue = int(input("Enter a number : "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue

print("Multiplication table of " + str(inputValue) + " is ")
for num in range(1, 11):
    print(num*inputValue)
