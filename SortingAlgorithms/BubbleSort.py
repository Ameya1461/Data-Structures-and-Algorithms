# Bubble Sorting Algorithm --> repeatedly swap adjacent pairs if they are in wrong order

def bubbleSort(customList):  # O(n^2), O(1)
    for i in range(len(customList) - 1):
        for j in range(len(customList) - 1 - i):
            if customList[j] > customList[j+1]:
                customList[j] , customList[j+1] = customList[j+1] , customList[j]
    print(customList)

cList = [5,1,3,2]
bubbleSort(cList)