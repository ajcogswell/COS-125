import random as rand
# File: ajCogswell_Simulation.py
# Author: Aj Cogswell
# Date: 11/24/2025
# Section: 1001
# E-mail: anthony.cogswell@maine.edu
# Description: Simulation of weather changes on local populations
# Collaborations: None

def main():
    masterDict = dict()
    world = False

    while world != '[CITY]' and world != '[FARM]': 
        world = worldChoice()

    weatherDict, maxTurns = weatherSetup()
    worldDict, sceneNames = worldSetup(world) # pyright: ignore[reportGeneralTypeIssues]
    birthRate, deathRate = getDeathBirthRate()
    masterDict['simRules'] = dict()
    masterDict['World'] = worldDict
    masterDict['Weather'] = weatherDict
    masterDict['simRules']['maxTurns'] = maxTurns
    masterDict['simRules']['birthRate'] = birthRate
    masterDict['simRules']['deathRate'] = deathRate
    masterDict['simRules']['Turn'] = 0
    masterDict = weatherImpact(masterDict, world)
    print(masterDict['World'])

def weatherImpact(masterDict, world):

    lowRainfall = 1.0
    highRainfall = 4.0
    highHeat = 30.0
    worldCats = list(masterDict['World'][world].keys())
    humanPop = masterDict['World'][world][worldCats[0]]
    animalPop = masterDict['World'][world][worldCats[1]]
    pestPop = masterDict['World'][world][worldCats[2]]
    weatherInfo = list(masterDict['Weather'].keys())
    rainfall = masterDict['Weather'][weatherInfo[0]]
    temp = masterDict['Weather'][weatherInfo[1]]
    rounds = 0

    while rounds < 1 or rounds > (masterDict['simRules']['maxTurns'] - masterDict['simRules']['Turn']):
        rounds = int(input(f"How many weeks would you like to simulate (max {masterDict['simRules']['maxTurns'] - masterDict['simRules']['Turn']}) : "))
    i = 0
    while i < rounds:
        weeklyRainfall = rainfall[masterDict['simRules']['Turn']]
        weeklyTemp = temp[masterDict['simRules']['Turn']]

        if weeklyRainfall < lowRainfall:
            animalPop = animalPop//1.1
        
        if weeklyRainfall > highRainfall and weeklyTemp > highHeat:
            pestPop = pestPop * rand.randint(10,21)
        
        if ((humanPop + animalPop) * 1.3) < pestPop:
            pestPop(masterDict)

        print(f"Temperature: {weeklyTemp}, Rainfall: {weeklyRainfall} \nPeople: {humanPop}, {worldCats[1]}: {animalPop}, Pests: {pestPop}")

        masterDict['simRules']['Turn']+=1
        i+=1

    return masterDict
    
# def pestPop(masterDict):



def worldChoice():
    environment = input("Are we simulating weather within the city, or the farm? type 'city' or 'farm': \n").strip().upper()

    if environment == 'CITY' or environment == 'FARM':
        return (f"[{environment}]")
    else:
        print(f"[{environment}]")
        print("Invalid selection. Please type 'city' or 'farm'.")
        return False

def worldSetup(scene):
    startFile = "starterFile.txt"
    cityDict = {}
    farmDict = {}
    sceneNames = list()

    with open(startFile, 'r') as f:
        lines = f.readlines()
        midpoint = len(lines) // 2
        pos = 0

        for line in lines:
            if line == lines[0]:
                cityDict[line.strip()] = {}
                sceneNames.append(line.strip())
            elif line == lines[midpoint]:
                farmDict[line.strip()] = {}
                sceneNames.append(line.strip())
            else:
                if pos < midpoint:
                    cat, num = line.split(":")
                    cityDict[lines[0].strip()][cat] = int(num.strip())
                elif pos > midpoint:
                    cat, num = line.split(":")
                    farmDict[lines[midpoint].strip()][cat] = int(num.strip())

            pos += 1

    if scene == '[CITY]':
        return(cityDict, sceneNames)
    elif scene == '[FARM]':
        return(farmDict, sceneNames)
    else:
        print('Something went wrong-- try re-running the program.')

def weatherSetup():
    weatherFile = "weather.csv"
    weatherDict = dict()
    headers = []
    listA = list()
    listB = list()
    listC = list()

    with open(weatherFile, 'r') as f:
        content = f.readlines()
        pos = 0

        for i in content:
            if pos == 0:
                a, b, c = i.strip().split(",")
                headers = [a, b, c]
                weatherDict[b] = {}
                weatherDict[c] = {}
            else:
                 a, b, c = i.strip().split(",")
                 listA.append(float(a))
                 listB.append(float(b))
                 listC.append(float(c))

            pos +=1

    weatherDict[headers[1]] = listB
    weatherDict[headers[2]] = listC
    maxTurns = len(listA)

    return weatherDict, maxTurns

def getDeathBirthRate():
    birthRate = 0
    deathRate = 0

    while birthRate < 1 or birthRate > 100:
        birthRate = int(input("Please provide a general birth rate for the simulation (1-100): "))
    while deathRate < 1 or deathRate > 100:
        deathRate = int(input("Please provide a general death rate for the simulation (1-100): "))

    return birthRate, deathRate

main()