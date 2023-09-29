# Q 12: Implement a function to check if a given year is a leap year or not

print("Check if a given year is a leap year or not \n")

global year

while (1):
    try:
        year = int(input("Enter year : "))
        break
    except:
        print("Incorrect inputs! Try again")
        continue


def leapYear(year):
    return year % 4 == 0


if leapYear(year):
    print("Given year is leap year")
else:
    print("Given year is not leap year")
