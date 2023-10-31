num = [2,4,5,6,7,8]

def squire(number):
    return number*number

squire_of_iterator = map(squire,num)

squr = list(squire_of_iterator)
print(squr)