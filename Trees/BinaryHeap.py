## Implementation of Binary Heap  --- Min Heap , Max Heap

# Creating Binary Heap
class Heap:
    def __init__(self,size):  # O(1) & O(N)
        self.customList = (size+1) * [None]   ## +1 because we r not using the 0th index(starting from 1st index)
        self.heapSize = 0
        self.maxSize = size + 1

# PEEK Method --> Returns the rootNode (top element)
def peekOfHeap(rootNode):  # O(1) both
    if not rootNode:
        return 
    else:
        return rootNode.customList[1]

# Size of Binary Heap( *Imp*: but here we should calculate the size of filled block only, donot consider empty ones in the size)    
def sizeOfHeap(rootNode):  # O(1) both
    if not rootNode:
        return 0
    else:
        return rootNode.heapSize
    
# Traversal
def levelOrderTraversal(rootNode):  # O(N), O(1)
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize + 1):
            print(rootNode.customList[i])

## Insertion starts here 
# Helper method : heapify method

def heapifyTreeInsert(rootNode, index , heapType): 
    parentIndex = int(index / 2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)   # O(logN)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)   # O(logN)

def insertNode(rootNode, nodeValue, heapType): # O(logN) O(logN)
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is full!"
    rootNode.heapSize + 1 = nodeValue
    rootNode.heapSize += 1 
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType) # O(logN)
    return "Successfully inserted the node value in Binary Heap! :)))"

#####################################

# Extract a Node from BH
# heapify method
def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = 2 * index
    rightIndex = 2 * index + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
                return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
                return
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] <  rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp    
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp    
        heapifyTreeExtract(rootNode, swapChild, heapType)


def extractNode(rootNode, heapType):  # O(logN) , O(logN)
    if rootNode.heapSize == 0:
        return "The BH is empty"
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapsize]
        rootNode.customList[rootNode.heapsize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)  # O(logN)
        return extractedNode
##############################################################################

# Delete entire binary heap
def delete(roottNode):   # O(1), O(1)
    roottNode.customList = None
    return "Deleted the entire Binary Heap!!"

newBinaryHeap = Heap(5)
print(newBinaryHeap.heapSize)