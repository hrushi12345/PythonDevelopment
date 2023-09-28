# Q 10: Write a program that converts a given number of days 
# into years, months, and days.

print("Convert days to Years, Months, Weeks \n")

while(1):
    try:
        days = int(input("Enter number of days: "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue
    
years = int(days/365)
months = int((days - years*365)/30)
day1 = days - years*365 - months*30

print("Number of years are : ", years)
print("Number of months are : ", months)
print("Number of days are : ", day1)

