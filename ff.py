def findTotal(*args):
    total=0
    for num in args:
        total+=num
    return total
print(findTotal(1,2,3,4,5))