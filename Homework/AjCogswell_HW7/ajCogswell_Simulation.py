import random as rand

# File: ajCogswell_Simulation.py
# Author: Aj Cogswell
# Date: 11/24/2025
# Section: 1001
# E-mail: anthony.cogswell@maine.edu
# Description: Simulation of weather changes on local populations. Stores each turn within history.txt, and updates state.txt for next session.
# Collaborations: None


def main():
    replay = None
    savePresent = checkSave()
    if savePresent:
        while replay is None:
            userInput = input("Would you like to resume your last session? ").lower()
            if userInput == "yes" or userInput == "y":
                replay = True
            elif userInput == "no" or userInput == "n":
                replay = False
            else:
                print("Invalid selection")
    else:
        replay = False
    masterDict = dict()
    world = False

    if not replay:
        while world != "[CITY]" and world != "[FARM]":
            world = worldChoice()
        weatherDict, maxTurns = weatherSetup()
        worldDict = worldSetup(world)  # pyright: ignore[reportGeneralTypeIssues]
        birthRate, deathRate = getDeathBirthRate()
        masterDict["simRules"] = dict()
        masterDict["World"] = worldDict
        masterDict["Weather"] = weatherDict
        masterDict["simRules"]["maxTurns"] = maxTurns
        masterDict["simRules"]["birthRate"] = birthRate
        masterDict["simRules"]["deathRate"] = deathRate
        masterDict["simRules"]["Turn"] = 0
    elif replay:
        masterDict = loadSession()
        world = list(masterDict["World"].keys())[0]

    playing = True
    masterDict = weatherImpact(masterDict, world)
    while playing:
        keepPlaying = input("Would you like to keep simulating? ").lower()
        if keepPlaying == "yes" or keepPlaying == "y":
            masterDict = weatherImpact(masterDict, world)
        elif keepPlaying == "no" or keepPlaying == "n":
            playing = False
        else:
            print("Invalid selection")


def worldSetup(scene):
    startFile = "starterFile.txt"
    cityDict = {}
    farmDict = {}
    sceneNames = list()

    with open(startFile, "r") as f:
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

    if scene == "[CITY]":
        return cityDict
    elif scene == "[FARM]":
        return farmDict
    else:
        print("Something went wrong-- try re-running the program.")


def worldChoice():
    environment = (
        input(
            "Are we simulating weather within the city, or the farm? type 'city' or 'farm': \n"
        )
        .strip()
        .upper()
    )

    if environment == "CITY" or environment == "FARM":
        return f"[{environment}]"
    else:
        print(f"[{environment}]")
        print("Invalid selection. Please type 'city' or 'farm'.")
        return False


def getDeathBirthRate():
    birthRate = 0
    deathRate = 0

    while birthRate < 1 or birthRate > 100:
        birthRate = int(
            input("Please provide a general birth rate for the simulation (1-100): ")
        )
    while deathRate < 1 or deathRate > 100:
        deathRate = int(
            input("Please provide a general death rate for the simulation (1-100): ")
        )

    return birthRate, deathRate


def weatherSetup():
    weatherFile = "weather.csv"
    weatherDict = dict()
    headers = []
    listA = list()
    listB = list()
    listC = list()

    with open(weatherFile, "r") as f:
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

            pos += 1

    weatherDict[headers[1]] = listB
    weatherDict[headers[2]] = listC
    maxTurns = len(listA)

    return weatherDict, maxTurns


def weatherImpact(masterDict, world):
    lowRainfall = 1.0
    highRainfall = 3.2
    highHeat = 30.0
    worldCats = list(masterDict["World"][world].keys())
    humanPop = masterDict["World"][world][worldCats[0]]
    birthRate = masterDict["simRules"]["birthRate"]
    deathRate = masterDict["simRules"]["deathRate"]
    animalPop = masterDict["World"][world][worldCats[1]]
    pestPop = masterDict["World"][world][worldCats[2]]
    weatherInfo = list(masterDict["Weather"].keys())
    rainfall = masterDict["Weather"][weatherInfo[0]]
    temp = masterDict["Weather"][weatherInfo[1]]
    rounds = 0

    while (
        rounds < 1
        or rounds
        > (masterDict["simRules"]["maxTurns"] - masterDict["simRules"]["Turn"]) - 1
    ):
        rounds = int(
            input(
                f"How many weeks would you like to simulate (max {masterDict['simRules']['maxTurns'] - masterDict['simRules']['Turn']}) : "
            )
        )
    i = 0
    while i < rounds:
        humanPop = (humanPop + humanPop * (birthRate - deathRate) / 100) // 1
        animalPop = (animalPop + animalPop * (birthRate - deathRate) / 100) // 1
        pestPop = (pestPop + pestPop * (birthRate - deathRate) / 100) // 1
        weeklyRainfall = rainfall[masterDict["simRules"]["Turn"]]
        weeklyTemp = temp[masterDict["simRules"]["Turn"]]

        if weeklyRainfall < lowRainfall:
            animalPop = animalPop // 1.1

        if weeklyRainfall > highRainfall and weeklyTemp > highHeat:
            pestPop = (pestPop + pestPop * (rand.randint(10, 21) / 100)) // 1
            humanPop, animalPop, pestPop = pestControl(humanPop, animalPop, pestPop)

        print(
            f"Temperature: {weeklyTemp}, Rainfall: {weeklyRainfall} \nPeople: {humanPop}, {worldCats[1]}: {animalPop}, Pests: {pestPop}"
        )
        masterDict["simRules"]["Turn"] += 1
        updateHistory(
            masterDict,
            humanPop,
            animalPop,
            pestPop,
            birthRate,
            deathRate,
            masterDict["simRules"]["Turn"],
            temp,
            rainfall,
            masterDict["simRules"]["maxTurns"],
            world,
            worldCats[1],
        )
        i += 1

    masterDict["World"][world][worldCats[0]] = humanPop
    masterDict["World"][world][worldCats[1]] = animalPop
    masterDict["World"][world][worldCats[2]] = pestPop

    return masterDict


def pestControl(humanPop, animalPop, pestPop):
    decrease = 0.05
    if ((humanPop + animalPop) * 1.3) < pestPop:
        print("Pests population has resulted in some casualties.")
        humanPop = (humanPop - (humanPop * decrease)) // 1
        pestPop = (pestPop - (pestPop * decrease)) // 1
    return (humanPop, animalPop, pestPop)


def updateHistory(
    masterDict,
    humanPop,
    animalPop,
    pestPop,
    birthRate,
    deathRate,
    turn,
    temperature,
    rainfall,
    maxTurns,
    world,
    animalName,
):
    historyFile = "history.txt"
    saveFile = "state.txt"
    with open(historyFile, "a") as f:
        f.write(f"{str(masterDict)}\n")
    with open(saveFile, "w") as f:
        f.writelines(
            f"World:{world}\nhumans:{humanPop}\n{animalName}:{animalPop}\npests:{pestPop}\nbirthRate:{birthRate}\ndeathRate:{deathRate}\nTurn:{turn}\nRainfall_cm:{rainfall}\nHeat_C:{temperature}\nmaxTurns:{maxTurns}"
        )


def checkSave():
    saveFile = "state.txt"
    with open(saveFile, "r") as f:
        content = f.read(1)
        return bool(content)


def loadSession():
    saveDict = dict()
    saveTemp = None
    saveFile = "state.txt"
    saveKeys = []
    saveValues = []

    with open(saveFile, "r") as f:
        saveTemp = f.readlines()

    for line in saveTemp:
        cat, num = line.strip().split(":")
        saveKeys.append(cat)
        saveValues.append(num)

    pos = 0
    for i in saveKeys:
        if i == "World":
            saveDict[i] = saveValues[pos].strip()
        elif i != "Rainfall_cm" and i != "Heat_C":
            saveDict[i] = float(saveValues[pos])
        elif i == "Rainfall_cm" or i == "Heat_C":
            tempList = []
            temp = saveValues[pos].strip()[1:-1].split(",")
            for j in temp:
                tempList.append(float(j))
            saveDict[i] = tempList
        else:
            print("There was a problem while loading your previous session.")
        pos += 1

    worldName = saveDict[saveKeys[0]]

    masterDict = {
        "simRules": {
            saveKeys[9]: saveDict[saveKeys[9]],
            saveKeys[4]: saveDict[saveKeys[4]],
            saveKeys[5]: saveDict[saveKeys[5]],
            saveKeys[6]: int(saveDict[saveKeys[6]]),
        },
        "World": {
            worldName: {
                saveKeys[1]: int(saveDict[saveKeys[1]]),
                saveKeys[2]: int(saveDict[saveKeys[2]]),
                saveKeys[3]: int(saveDict[saveKeys[3]]),
            }
        },
        "Weather": {
            saveKeys[7]: saveDict[saveKeys[7]],
            saveKeys[8]: saveDict[saveKeys[8]],
        },
    }
    return masterDict


main()
