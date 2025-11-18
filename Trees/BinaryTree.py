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

# Delete a Node in BT has to done by these 3 method belows -- find deepestnode, delete deepest node, delete node we want and replace by deepestnode
def getDeepestNode(rootNode):
    if not rootNode:
        return "The BT doesen't exist!"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return "BT dosen't exist!"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value == dNode:
                root.value = None
                return "Successfully Deleted!!!"
            if root.value.leftChild is not None:
                if root.value.leftChild == dNode:
                    root.value.leftChild = None
                    return "Deleted!!"
                else:
                    customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                if root.value.rightChild == dNode:
                    root.value.rightChild = None
                    return "Deleted!!"
                else:
                    customQueue.enqueue(root.value.rightChild)

def deleteNodeBT(rootNode, node):   # O(N), O(N)
    if not rootNode:
        return "BT doesn't exist!"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):  #O(N)
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)  # O(N) --- 2nd O(n) still total is O(N)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "Deleted the node and replaced with deepest Node!"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "Deleted the entire BT"

print(deleteBT(newBT))
print(newBT.data)
# levelOrderTraversal(newBT)   
# print("---------") 
# deleteNodeBT(newBT, 'Cold')
# levelOrderTraversal(newBT)
            
# preOrderTraversal(newBT)
# print("-------")
# inOrderTraversal(newBT)
# print("-------")
# postOrderTravsersal(newBT)
# print("-------")
# levelOrderTraversal(newBT)
# print("-------")
# print(searchBT(newBT,'Tea'))

# newNode = TreeNode('Cola')
# print(insertBT(newBT, newNode))
# levelOrderTraversal(newBT)