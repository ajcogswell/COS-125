# File Name: ajCogswell_lab4
# Author: Aj Cogswell
# Date: 9/18/25
# Section: 0001
# E-mail: anthony.cogswell@maine.edu
# Description: 
# Collaboration: None

TAX_EXEMPT_AGE = 16
TAX_EXEMPT_BRACKET = 0
TAX_EXEMPT_BRACKET_CAP = None

EARNING_TEEN_AGE = 25
EARNING_TEEN_BRACKET1 = 10
TEEN_BRACKET1_CAP = 20000
EARNING_TEEN_BRACKET2 = 15

ADULT_AGE = 26
ADULT_BRACKET1 = 20
ADULT_BRACKET1_CAP = 50000
ADULT_BRACKET2 = 25

userAge = None
userIncome = None

count = 5

numGiven = None
numGiven = int(input("Enter a number: "))

if numGiven == 0:
    print(f"number is {numGiven}")
elif numGiven != 0:
    if numGiven > 0:
        print("Number given is positive")
    if numGiven%2 == 0:
        print("Number given is even!")
    if numGiven%2 != 0:
        print("Number given is odd.")
else:
    print("Something went wrong, try again later.")

userAge = int(input("Please enter your age: "))
userIncome = int(input("Please enter your yearly income: "))

if userAge <= TAX_EXEMPT_AGE:
    print(f"You are part of the Tax exempt bracket.")
else:
    if userAge <= EARNING_TEEN_AGE:
        if userIncome <= TEEN_BRACKET1_CAP:
            print(f"You are part of the earning teen tax bracket, with a {EARNING_TEEN_BRACKET1}% tax rate.")
        else:
            print(f"You are part of the earning teen tax bracket, with a {EARNING_TEEN_BRACKET2}% tax rate.")
    elif userAge > EARNING_TEEN_AGE:
        if userIncome <= ADULT_BRACKET1_CAP:
            print(f"You are part of the working adult tax bracket, with a {ADULT_BRACKET1}% tax rate.")
        else:
            print(f"You are part of the working adult tax bracket, with a {ADULT_BRACKET2}% tax rate.")

while count >=0:
    print(count)
    count-=1

num = 1

while num <= 3:
    num2 = 1
    while num2 <= 3:
        result = num * num2
        print(result, end = "  ")
        num2 += 1
    print()
    num += 1

