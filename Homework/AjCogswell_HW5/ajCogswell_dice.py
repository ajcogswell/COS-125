import random
# File: ajCogswell_dice.py
# Author: Aj Cogswell
# Date: 10/22/2025
# Section: 1001
# E-mail: anthony.cogswell@maine.edu
# Description: Rolls 50 dice, creates point system, asks user 
# how many dice to roll, checks to see if score%7==0, if so, the user wins game.
# Collaboration: Showed to Dr. Gurney. 

INITROLL = 50
diceDict = {
    "dice": [1,2,3,4,5,6],
    "pointVals": [],
    "diceCount": [[1,[0]],[2,[0]],[3,[0]],[4,[0]],[5,[0]],[6,[0]]],
    "diceCountDefault": [[1,[0]],[2,[0]],[3,[0]],[4,[0]],[5,[0]],[6,[0]]],
    "currentRoll": []
}
objective = 7

def main():
    diceDict["diceCount"] = diceDict["diceCountDefault"][::]
    diceDict["pointVals"].clear()
    countList = diceDict["diceCount"].copy()
    for i in range(INITROLL):
        roll = random.choice(diceDict["dice"])
        diceDict["diceCount"][roll-1][1][0] += 1
    for num in range(len(diceDict["dice"])):
         highestCount = -1
         diceToRemove = None
         for i in countList:
             count = i[1][0]
             if count > highestCount:
                 highestCount = count
                 diceToRemove = i
         if diceToRemove:
             diceDict["pointVals"].append(diceToRemove[0])
             countList.remove(diceToRemove)
    diceToRoll = int(input("How many dice would you like to roll?\n"))
    roll_dice(diceToRoll)

def roll_dice(numOfDice):
    for i in range(numOfDice):
        roll = random.choice(diceDict["dice"])
        diceDict["currentRoll"].append(roll)
    get_score()

def get_score():
    tempScore = 0
    score = 0
    for i in diceDict["currentRoll"]:
        count = 0
        for j in diceDict["pointVals"]:
            count +=1
            if j == i:
                tempScore = tempScore + i*count
    score = tempScore
    decide_win(score)

def decide_win(points):
    if points%objective == 0:
        print("You Win!")
    elif points%objective != 0:
        print("You lost.")
    
    replayPrompt = input("Would you like to play again?\n").lower()

    if replayPrompt == 'y' or replayPrompt == 'yes':
        replay(True)
    elif replayPrompt == 'n' or replayPrompt == 'no':
        replay(False)

def replay(bool):
    if bool:
        main()
main()
