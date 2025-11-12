nums=[12,1,3,4,5,22,19,2,50]

numToFind = int(input("Enter a number:"))

def numChecker(list, int):
    inList = False
    for i in list:
        if i == int:
            inList = True
    
    return inList

print(numChecker(nums, numToFind))

    