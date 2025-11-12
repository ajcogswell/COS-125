# File Name: ajCogswell_lab3
# Author: Aj Cogswell
# Date: 9/18/25
# Section: 0001
# E-mail: anthony.cogswell@maine.edu
# Description: 
# Collaboration: None

hasLicense = 0
rightOnRed = 0
roadwayClear = 0

ageAlc = int(input("Enter your age: "))
if ageAlc >= 21:
    print("Youy can buy alcohol.")
else:
    print("You can't buy alcohol.")

grade = int(input("What was your grade percentage?  "))

if grade >= 90:
    print("You got an A!")
elif grade >= 80:
    print("You got an B.")
elif grade >= 70:
    print("You got an C.")
else:
    print("You failed.")

ageLicense = int(input("Enter your age: "))

if ageLicense >= 16:
    hasLicense = int(input("Do you have a license?\n Yes: 1\n No: 2\n"))
    if hasLicense == 1:
        print("You can drive.")
    else:
        print("You cannot drive without a license.")
else:
    print("You are too young to drive.")

# # Challenge scenerio

# # Challenge 1

numInput = int(input("Please input a number.\n"))
remainder = numInput%2

if numInput == 0:
    print(f"Input is {numInput}")
else:
    if remainder == 0:
        print(f"{numInput} is even.")
    else:
        print(f"{numInput} is odd.")


# # Challenge 2

lightState = input("What color is the traffic light?\n")

if lightState == "red" or lightState == "Red":
    rightOnRed = int(input("Is right on red allowed?\nYes: 1\nNo: 0\n"))
    if rightOnRed == 1:
        roadwayClear = int(input("Is there oncoming traffic?\nYes: 1\nNo: 0\n"))
        if roadwayClear == 0:
            print("Proceed with caution after stopping.")
        else:
            print("Stop.")
    else:
        print("Stop.")
elif lightState == "yellow" or lightState == "Yellow":
    print("Caution!")
elif lightState == "green" or lightState == "Green":
    print("Go on, gyet.")
else:
    print("Invalid color given.")

