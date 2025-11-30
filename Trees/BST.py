# Implementation of Binary Search Tree:
import QueueLinkedList as queue 
class BSTNode:
    def __init__(self,data):   # O(1) --> Creation of BST
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insert(rootNode, nodeValue):  # O(Log N)
    if not rootNode:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)   # show be a node and not a value, hence added BSTNode()
        else:
            insert(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)  # show be a node and not a value, hence added BSTNode()
        else:
            insert(rootNode.rightChild, nodeValue)
    return "Inserted"

# DFS 1 -- USING STACK  --> root,left,right
def preOrderTraversal(rootNode):  # O(N) for all traversals
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

# Delete a node in BST --> find minimun in rightsubtree first
def minValueNode(bstNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild
    return current

def deleteNodeBST(rootNode, nodeValue):  # O(log N) for both
    if not rootNode:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNodeBST(rootNode.leftChild, nodeValue)  # O(n/2)
    elif nodeValue > rootNode.data:  
        rootNode.rightChild = deleteNodeBST(rootNode.rightChild, nodeValue)  # O(n/2)
    else: ## Delete a node with 1 child or none child(leaf node)
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = minValueNode(rootNode.rightChild)  # We got the min (successor)  # O(LogN)
        rootNode.data = temp.data  # replace value of that node with minimun value
        rootNode.rightChild = deleteNodeBST(rootNode.rightChild, temp.data)  ## Goes to the right subtree and calls delete recursively to get temp node from rightChild # O(n/2)
    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "BST is deleted successfully"

newBST = BSTNode(None)

