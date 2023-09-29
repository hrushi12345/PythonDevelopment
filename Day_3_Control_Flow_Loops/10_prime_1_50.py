# Q 10: Create a loop that prints all prime numbers between 1 and 50.

print("Prints all prime numbers between 1 and 50 \n")

primeList = []
for i in range(2, 50):
    isPrime = True
    for j in range(2, int(i/2) + 1):
        if i % j == 0:
            isPrime = False
    if isPrime:
        primeList.append(i)

print("Prime list is ", primeList)
