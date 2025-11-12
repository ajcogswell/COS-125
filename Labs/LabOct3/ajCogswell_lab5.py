# File: ajCogswell_lab5.py
# Author: Aj Cogswell
# Date: 10/2/2025
# Section: 1001
# E-mail: anthony.cogswell@maine.edu
# Description: 
# Collaboration: None

KPHLIST = [0.0,10,20,30,40,50,60,70,80,90,100]
mphList = []
stringList = []
integerList = []
squaredList = []


for i in range(len(KPHLIST)):
    mphConversion = KPHLIST[i]*0.6214
    mphList.append(mphConversion)

print("KPH  |  MPH")

for i in range(len(KPHLIST)):
    kphToPrint = KPHLIST[i]
    mphToPrint = mphList[i]
    print(f"{float(kphToPrint):3.0f}", end="  |")
    print(f"  {float(mphToPrint):3.2f}") 

stringList = input("Enter a list of numbers, seperated by spaces:").split(" ")


for i in stringList:
    integerList.append(int(i))
    numToSquare = integerList[i]
    numSquared = numToSquare**2

    squaredList.append(numSquared)
