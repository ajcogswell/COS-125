# File: ajCogswell_sentenceGenerator.py
# Author: Aj Cogswell
# Date: 9/27/2025
# Section: 1001
# E-mail: anthony.cogswell@maine.edu
# Description: Creates sentences based off user inputs!
# Collaboration: None

import random

nounList = []
adjectiveList = []
verbList = []
sentStarter = ""

sentStarter = input("Give a starter word for your sentences: (ex. 'the'): ")
nounList = input("Please give five nouns for our sentences, seperated by comma: ").split(",")
adjectiveList = input("Please give five adjectives for our sentences, seperated by comma: ").split(",")
verbList = input("Please give five verbs for our sentences, seperated by comma: ").split(",")

print(nounList)
print(adjectiveList)
print(verbList)

for i in range(5):
    print(f"{sentStarter} {adjectiveList[i]} {nounList[i]} {verbList[i]}")