# Implementation of a binary tree --> each node has at the most 2 subnodes(child)
import QueueLinkedList as queue 

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode('Drinks')
leftChild = TreeNode('Hot')
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
leftChild.leftChild = coffee
leftChild.rightChild = tea
rightChild = TreeNode('Cold')
newBT.leftChild = leftChild
newBT.rightChild = rightChild

# DFS 1 -- USING STACK  --> root,left,right
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# DFS 2 -- USING STACK --> left,root,right
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# DFS 3 -- USING STACK -- left,right,root
def postOrderTravsersal(rootNode):
    if not rootNode:
        return
    postOrderTravsersal(rootNode.leftChild)
    postOrderTravsersal(rootNode.rightChild)
    print(rootNode.data)

# BFS --> Using queue
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

# Search a node -- using levelOrderTravseral --> Queue is faster than stack
def searchBT(rootNode,NodeValue):
    if not rootNode:
        return "The BT dosen't exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):  # O(N)
            root = customQueue.dequeue()
            if root.value.data == NodeValue:   
                return "Success! Found Here!!!"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Not found!! :("
    
def insertBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully inserted"
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully inserted"
            
# preOrderTraversal(newBT)
# print("-------")
# inOrderTraversal(newBT)
# print("-------")
# postOrderTravsersal(newBT)
# print("-------")
# levelOrderTraversal(newBT)
# print("-------")
# print(searchBT(newBT,'Tea'))

newNode = TreeNode('Cola')
print(insertBT(newBT, newNode))
levelOrderTraversal(newBT)