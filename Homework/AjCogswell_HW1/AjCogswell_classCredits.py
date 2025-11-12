# File: AjCogswell_classCredits.py
# Author: Aj Cogswell
# Date: Sept 8, 2025
# Section: COS 125 1001
# E-mail: anthony.cogswell@maine.edu
# Description:
# Prints total cost for credits based off user input. Asks user for name, and how many credits being taken
# Multiplies num_credits & CREDIT_COST to determine user's cost.

CREDIT_COST = 350.50

user_name = ""
num_credits = 0

# Prompts user for name
user_name = input("Please enter your name: ")
# Prompts 'em for how enrolled credits
num_credits = int(input("How many credits you are taking: "))
# Prints their name, enrolled credits, cost per credit, & total cost.
print(user_name, "\nYou are registered for", num_credits)
print("At $" , CREDIT_COST, "per credit, your total is $", (num_credits * CREDIT_COST))