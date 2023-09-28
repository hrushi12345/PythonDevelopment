# Q 10: Implement a program that converts a given number of minutes into hours and minutes.

import ast

print("Convert minutes to hours and minutes : ")

while (1):
    try:
        minutes = ast.literal_eval(input("Enter minutes : "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue

hours = int(minutes/60)
minute1 = minutes - hours*60

print("Number of hours after converting minutes are : ", hours)
print("Remaining minutes after converting minutes are : ", minute1)
