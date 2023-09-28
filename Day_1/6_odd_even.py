# Q 6: Write a program to check if a number is even or odd.

print("Check number is odd or even \n")

while(1):
    try:
        num = int(input("Enter a number : "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue

check = num%2 == 0

if check:
    print("Number is Even.")
else:
    print("Number is Odd.")