fruitRainbow = {
     "cherry":"red",
     "banana":"yellow",
     "melon":"green",
     "apple":"red",
     "pineapple":"yellow"
}
fruitSelection = None

print(fruitRainbow)
print(fruitRainbow.keys())

fruitSelection = input("Choose a fruit to find it's color: ").lower()

for i in fruitRainbow:

    if i == fruitSelection:
        print(fruitRainbow[i])

fruitName = input("Enter the name of the fruit: ").lower()
fruitColor = input(f"Enter the color {fruitName}: ").lower()
toAdd = {fruitName:fruitColor}
fruitRainbow.update(toAdd)

print(fruitRainbow)