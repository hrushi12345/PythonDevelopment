# Q 6: Create a program that generates the Fibonacci sequence up to a given number of terms.

print("Generates the Fibonacci sequence up to a given number of terms \n")

while (1):
    try:
        inputValue = int(input("Enter a number : "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue
count = 3
a = 0
b = 1
print("Fibonacci sequence is : \n"+str(a)+"\n"+str(b))
while (count <= inputValue):
    c = a + b
    print(c)
    a = b
    b = c
    count += 1
