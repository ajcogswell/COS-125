# File: ajCogswell_internet.py
# Author: Aj Cogswell
# Date: 9/18/2025
# Section: 1001
# E-mail: anthony.cogswell@maine.edu
# Description: Asks user to input networking requirements and recommends an internet package
# based on their responses.
# Collaboration: None

# Basic Internet Information
BASICSPEED = 50 
BASICDATA = 500
BASICCOST = 40.00
                                                                                                
# Standard Internet Information
STANDARDSPEED = 150 
STANDARDDATA = 1000 
STANDARDCOST = 65.00

# Premium Internet Information
PREMIUMSPEED = 500 
PREMIUMDATA = "unlimited" 
PREMIUMCOST = 90.00

# Customer Information
custName = None
desiredSpeed = None
desiredData = None
desiredBudget = None

# Outcome Placeholders
packageDecision = "Basic"
outcomeSpeed = BASICSPEED
outcomeData = str(f"{BASICDATA} GB of")
outcomeCost = BASICCOST
isInBudget = "is"

# Get info from customer
custName = input("Please enter your name: ")
desiredSpeed = int(input("Please enter the internet speed (in Mbps) you require: "))
desiredData = int(input("Please enter how much data per month you'd like: "))
desiredBudget = float(input("Please enter your budget: "))

# Compare customer requirements, compare to packages, and make a decision (changes from basic
# if needed)

if int(outcomeCost) > int(desiredBudget): 
    isInBudget = "is not"

if desiredSpeed > BASICSPEED or desiredData > BASICSPEED:
    if desiredSpeed <= STANDARDSPEED and desiredData <= STANDARDDATA:
        packageDecision = "Standard"
        outcomeSpeed = STANDARDSPEED
        outcomeCost = STANDARDCOST
        outcomeData = str(f"{STANDARDDATA} GB of")
    else:
        packageDecision = "Premium"
        outcomeSpeed = PREMIUMSPEED
        outcomeCost = PREMIUMCOST
        outcomeData = PREMIUMDATA

# Prints customer recommendation based on provided info
print(f'''\nThank you, {custName}. Based on your needs, we recommend the
{packageDecision} Package with {outcomeSpeed} Mbps speed and {outcomeData} data. It
costs ${outcomeCost:.2f} per month, which {isInBudget} within your budget of ${desiredBudget:.2f}.''')