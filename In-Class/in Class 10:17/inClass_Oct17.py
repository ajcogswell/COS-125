# Dictionaries are key:value pairs
# Referenced by key
# Does not use indices
# Keys must be unique
# List is []
# Tuple is ()
# Dictionary is {} by

groceries = {
    'dairy': 12,
    'hot dog': 3,
    'candy': 60,
    5:'harry',
    7:7,
    79:0
}

# print(groceries['dairy'])

print(groceries.items())
print(groceries.keys())

vals = groceries.values()
print(vals)

for i in vals:
    print(i)