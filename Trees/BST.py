# Implementation of Binary Search Tree:
import QueueLinkedList as queue 
class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insert(rootNode, nodeValue):  # O(Log N)
    if not rootNode:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)   # same reason here as well
        else:
            insert(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)  # show be a node and not a value, hence added BSTNode()
        else:
            insert(rootNode.rightChild, nodeValue)
    return "Inserted"

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

def searchNode(rootNode, nodeValue):  # O(Log N)
    if rootNode.data == nodeValue:
        return "Found!"
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            return "Found!"
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            return "Found!"
        else:
            searchNode(rootNode.rightChild, nodeValue)



newBST = BSTNode(None)

