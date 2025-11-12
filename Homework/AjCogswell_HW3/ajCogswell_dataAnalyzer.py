# File: ajCogswell_dataAnalyzer.py
# Author: Aj Cogswell
# Date: 9/27/2025
# Section: 1001
# E-mail: anthony.cogswell@maine.edu
# Description: Creates a dataset from user input, and gives user
# the even, odd, min, max, and average of dataset.
# Collaboration: None

dataList = []
evenNumbers = []
oddNumbers = []
listLength = None
evenNumLength = 0
oddNumLength = 0

loopProgress = 0
minInt = None
maxInt = None
intSum = 0
intAverage = 0

# Asks user how many data points in dataset
listLength = int(input("How many data points: "))

# Add numbers to data list
while loopProgress < listLength:
            userInput = input("Input data point: ")
            integer = int(userInput)
            dataList.append(integer)
            loopProgress +=1

# Reuses loopProgress for finding smallest number in dataset
loopProgress = 0
# Loop for finding min in dataset
while loopProgress < len(dataList):
        if minInt == None:
                minInt = dataList[loopProgress]
                loopProgress+=1
        else:
                if dataList[loopProgress] < minInt:
                    minInt = dataList[loopProgress]
                    loopProgress +=1
                elif dataList[loopProgress] > minInt:
                        loopProgress +=1  
 
# Reuses loopProgress for finding largest number in dataset    
loopProgress = 0
# Loop for finding max in dataset
while loopProgress < len(dataList):
        if maxInt == None:
                maxInt = dataList[loopProgress]
                loopProgress+=1
        else:
                if dataList[loopProgress] > maxInt:
                    maxInt = dataList[loopProgress]
                    loopProgress +=1
                elif dataList[loopProgress] < maxInt:
                        loopProgress +=1   

loopProgress = 0

while loopProgress < listLength:
        intSum = intSum + dataList[loopProgress]
        loopProgress+=1

loopProgress = 0

while loopProgress < len(dataList):
        if dataList[loopProgress]%2 == 0:
                evenNumToAdd = dataList[loopProgress]
                evenNumbers.append(evenNumToAdd)
                loopProgress+=1
        elif dataList[loopProgress]%2 != 0:
                oddNumToAdd = dataList[loopProgress]
                oddNumbers.append(oddNumToAdd)
                loopProgress+=1
        else:
                print("Number found that is neither even nor odd. Check data.")
                loopProgress+=1

print(f"\nDataset: {dataList}")
print(f"Sum: {intSum}")
print(f"Average: {intSum/listLength}")
print(f"Minimum value: {minInt}")
print(f"Largest Value: {maxInt}\n")
print(f"Even Numbers: {evenNumbers}, (count: {len(evenNumbers)})")
print(f"Odd Numbers: {oddNumbers} (count: {len(oddNumbers)})")