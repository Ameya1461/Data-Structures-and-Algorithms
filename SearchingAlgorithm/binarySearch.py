# Implementation of Binary Search --> Works only for sorted arrays
# TC: WC - O(LogN), BC - O(1)
# SC: O(1)

import math
def binarySearch(array, target):
    leftPointer = 0
    rightPointer = len(array) - 1
    middleIndex = math.floor((leftPointer + rightPointer) / 2)
    # print(leftPointer, middleIndex, rightPointer)
    while not(array[middleIndex] == target) and leftPointer <= rightPointer:
        if target < array[middleIndex]:
            rightPointer = middleIndex - 1
        else:
            leftPointer = middleIndex + 1
        middleIndex = math.floor((leftPointer + rightPointer) / 2)
    if array[middleIndex] == target:
        return middleIndex
    else:
        return -1


print(binarySearch([2,3,4,5,6,7,8,9,10], 15))

        #  0 1 2 3 4 5 6 7 8
# array = [2,3,4,5,6,7,8,9,10]
        #  L       M        R
# target = 3