# File: ajCogswell_Inventory.py
# Author: Aj Cogswell
# Date: 10/12/2025
# Section: 1001
# E-mail: anthony.cogswell@maine.edu
# Description: Creates warehouse inventory using user inputs.
# Collaboration: None

warehouseInv = []
warehouseName = ""
warehouseCategory = ""
warehouseItem = ""
CatCount = 0
warehouseCount = 0
warehouseCatCount = 0
warehouseItemCount = 0

warehouseCount = int(input("How many warehouses are there?\n"))

for i in range(warehouseCount):
    tempList = []
    tempList.clear()
    warehouseName = input(f"What is the name of warehouse {i+1}?\n").lower()
    tempList.append(warehouseName)
    warehouseInv.append(tempList[::])
    warehouseCatCount = int(input(f"How many categories within {warehouseInv[i][0]}\n"))
    tempList.clear()
    for j in range(warehouseCatCount):
        warehouseCategory = input("Enter category name: \n").lower()
        tempList.append(warehouseCategory)
    warehouseInv[i].append(tempList[::])
    CatCount = len(warehouseInv[i][1])
    for j in range(CatCount):
        warehouseItemCount = int(input(f"How many items within {warehouseInv[i][1][j]}: "))
        tempList.clear()
        for k in range(warehouseItemCount):
            warehouseItem = input(f"Enter item within {warehouseInv[i][1][j]}: ").lower()
            tempList.append(warehouseItem)
            warehouseItem = int(input(f"How many {warehouseItem}? "))
            tempList.append(warehouseItem)
        warehouseInv[i][1].append(tempList[::])

print("The total inventory")

for h in warehouseInv:
    warehouseName = h[0]
    print(f"{warehouseName}:")
    tempList = h[1]
    warehouseCatCount = len(tempList) // 2
    for i in range(warehouseCatCount):
        warehouseCategory = tempList[i]
        itemList = tempList[i + warehouseCatCount]
        outputParts = []
        for j in range(0, len(itemList), 2):
            itemName = itemList[j]
            itemCount = itemList[j+1]
            outputParts.append(f"{itemCount} {itemName}")
        finalOutput = ", ".join(outputParts)
        print(f"  {warehouseCategory}: {finalOutput}")

