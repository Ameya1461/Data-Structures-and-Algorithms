# AVL Tree Implementation --> Selfbalancing BST
import QueueLinkedList as queue 

class AVLNode:
    def __init__(self,data=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1  # To check if tree balanced or not(AVL Tree)

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
            return searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            return "Found!"
        else:
            return searchNode(rootNode.rightChild, nodeValue)

## Insertion start here 
def getHeight(rootNode):  
    if not rootNode:
        return 0
    return rootNode.height

## LEFT LEFT CONDITION -- ROTATE RIGHT
def rightRotate(disbalancedNode):  # O(1)
    newRootNode = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRootNode.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))  # 1 + because considering rootnode/parent as well 
    newRootNode.height = 1 + max(getHeight(newRootNode.leftChild), getHeight(newRootNode.rightChild))
    return newRootNode

## RIGHT RIGHT CONDITION -- ROTATE LEFT
def leftRotate(disbalancedNode):   # O(1)
    newRootNode = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRootNode.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRootNode.height = 1 + max(getHeight(newRootNode.leftChild), getHeight(newRootNode.rightChild))
    return newRootNode

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, nodeValue):  # O(Log N)
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)    # O(Log N)  # Recursive call
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)  # O(Log N)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftChild.data:  ## left left condn
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:  ## left right condn
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data:   ## right right
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:   ## right left
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode
########################## Insertion ends here ###################################

## Delete a Node in AVL
# Helper funtion

# def getMinValueNode(rootNode):
#     if rootNode is None or rootNode.leftChild is None:
#         return rootNode
#     return getMinValueNode(rootNode.leftChild)

# def deleteNode(rootNode, nodeValue):
#     if not rootNode:
#         return rootNode
#     elif 

# create a object
newAVL = AVLNode(10)