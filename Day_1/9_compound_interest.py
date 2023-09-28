# Q 9: Calculate the compound interest for a given principal 
# amount, interest rate, and time period.
import ast
print("Calculate coumpound interest \n")

while(1):
    try:
        principal = ast.literal_eval(input("Enter Principal amount: "))
        interest = ast.literal_eval(input("Enter Interest rate: "))
        time = ast.literal_eval(input("Enter Time period: "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue

interestRateCal = 1
for i in range(time):
    interestRateCal = interestRateCal * (1 + (interest/100))

compInterest = principal * interestRateCal

print("Compound Interest is : ", compInterest)