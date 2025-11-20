namesFile = open('names.txt', 'r')
print(namesFile)

for name in namesFile:
    print(name)

namesFile.close()

namesFile = open('names.txt', 'a')
addName = True
nameList = []

while addName:
    userInput = input("Enter a name:")
    nameList.append(userInput)
    replay = input("Do you want to add another name?").lower()
    if replay == "no" or replay == "n":
        addName = False
    elif replay == "yes" or replay == "y":
        addName = True
    else:
        print("Something went wrong...")

for i in nameList:
    namesFile.write(i)

namesFile.close()

