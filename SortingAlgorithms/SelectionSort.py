# SelectionSort --> Find the min between the elements and place it in first place - basically swap the min with first element.
                   # Continue this until all elements are sorted
                   # O(N^2), O(1)

def SelectionSort(customList):
    for i in range(len(customList)):
        minIndex = i
        for j in range(i+1, len(customList)):
            if customList[minIndex] > customList[j]:
                minIndex = j
        customList[i] , customList[minIndex] = customList[minIndex] , customList[i]
    print(customList)

cList = [6,2,4,1,9,3]
SelectionSort(cList)


# 1st --> [1,2,4,6,9,3]