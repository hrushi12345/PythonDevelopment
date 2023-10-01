# Q 1: Create a dictionary to store information about a person (name, age, address).

import ast

print("Store information about a person (name, age, address) \n")

while (1):
    try:
        name = input("Enter name of Person : ").strip()
        age = ast.literal_eval(input("Enter age of Person : "))
        address =  input("Enter address of Person : ").strip()
        break
    except:
        print("Incorrect inputs! Try again")
        continue

personalInfo = {}
personalInfo['Name'] = name
personalInfo['Age'] = age
personalInfo['Address']= address

print("Person's info in dictionary ", personalInfo)