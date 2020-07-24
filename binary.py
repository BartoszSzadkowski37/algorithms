import math
list = [1, 65, 3, 98, 12, 10, 100, 43, 11, 65, 4, 8, 30, 2]

list.sort()

print(list)

leftIndex = 0
rightIndex = len(list) - 1

middle = (leftIndex + rightIndex) / 2

middle = math.floor(middle)

looking = int(input('Looking number: '))

loop = True

while loop:
    if list[middle] == looking:
        loop = False
        print('Looking number is on position: ', middle)
    elif leftIndex > rightIndex:
        loop = False
        print('There is no the looking number in this list :C')
    else:
        if looking < list[middle]:
            rightIndex = middle - 1

        elif looking > list[middle]:
            leftIndex = middle + 1

        middle = (leftIndex + rightIndex) / 2
        middle = math.floor(middle)







