numList = [1,2,3,4,5,6,7]

def multiplyList(list):
    product = 1
    for i in list:
        product = product*i
    return product

print(multiplyList(numList))