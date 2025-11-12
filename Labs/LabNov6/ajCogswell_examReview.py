import random
# statement 1. list, dictionary
# statement 2. Dictionary
# statement 3. List, Tuple
# statement 4. List
# statement 5. List, Tuple, Dictionary
# statement 6. List

# # # # # # # # # # # # # # # # # 

data_list = [5, 10, 15, 20, 25]
subset = data_list[1:3]
subset[0] = 99
data_list.insert(0, 50)
print(data_list)

# Prints "[50, 5, 10, 15, 20, 25]""

# # # # # # # # # # # # # # # # # 

stats = {'HP': 100, 'MP': 50}
# Assuming stats is defined as above
if 'Stamina' in stats:
    print(stats['Stamina'])
else:
    print("Key Missing")

# Prints "Key Missing"

# # # # # # # # # # # # # # # # # 

def process_data(value):
    local_x = value * 2
    return local_x

global_x = 10
result = process_data(global_x)
print(global_x)

# Prints '10'

# # # # # # # # # # # # # # # # # 

def rockPaperScissors():
    items = ["rock", "paper", "scissors"]
    itemToUse = random.choice(items)
    return(itemToUse)

print(rockPaperScissors())

# # # # # # # # # # # # # # # # # 

def oddSumAcc(list):
    sumOdds = 0
    for i in list:
        if i%2 != 0:
            sumOdds += i
    return(sumOdds)

print(oddSumAcc([31,20,15]))

# # # # # # # # # # # # # # # # # 

def className():
    course_id = "COS 125"
    return(course_id)

courseID = className()

# # # # # # # # # # # # # # # # # 

def removeVowels(string):
    newString = ""
    for i in string:
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
            newString += i
    return(newString)

print(removeVowels("what ever mary lu, why dont you work at mcdonalds."))

# # # # # # # # # # # # # # # # # 

def createNumList():
    newList = []
    for i in range(100):
        newList.append(i)
    print(f"List of numbers from 0 - 99{newList}")
    return(newList)

def sortNumList(numList):
    oddNums = []
    evenNums = []
    oddNums = numList[1::2]
    evenNums = numList[::2]
    return evenNums, oddNums

numList = createNumList()
evenNums, oddNums = sortNumList(numList)

print(f"Even numbers List: {evenNums}")
print()
print(f"Odd numbers List: {oddNums}")

# # # # # # # # # # # # # # # # # 

def weaponChoice():
    weapons = ["bow", "sword", "gun", "harpoon", "cannon"]
    modifiers = ["ingited whale oil", "EMP", "Poison"]
    adjectives = ["Dwarven", "Elven", "Wobbly", "Toasted", "Jalepeno-flavored"]
    weaponToChoose = random.choice(weapons)
    weaponType = random.choice(adjectives)
    modifier = None
    maxDamage = 0
    minDamage = 0
    additDamage = 0
    modInt = random.randint(0,5)
    damage = [random.randint(0,50), random.randint(0,50)]
    if damage[0]>damage[1]:
        maxDamage = damage[0]
        minDamage = damage[1]
    elif damage[0]>=damage[1]:
        maxDamage = damage[1]
        minDamage = damage[0]
    if modInt == 1:
        modifer = random.choice(modifiers)
        additDamage = random.randint(0,15)
    
    return(weaponToChoose, 
           weaponType, 
           maxDamage, 
           minDamage, 
           modifier,
           additDamage)

weapon, weaponType, minDamage, maxDamage, mod, additDamage = weaponChoice()