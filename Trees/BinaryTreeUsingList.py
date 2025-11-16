## Implementation of Binary Tree using python list ###

class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insert(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The BT is full"
        else:
            self.customList[self.lastUsedIndex + 1] = value
            self.lastUsedIndex += 1
            return "Value inserted successfully!!! ;)"
        
    def search(self, node):
        if self.lastUsedIndex == 0:
            return "Binary tree empty"
        else:
            for i in range(1, self.lastUsedIndex + 1):
                if self.customList[i] == node:
                    return "Found"
            return "Not Found"

    def preOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)

    def inOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index * 2)
        print(self.customList[index])
        self.inOrderTraversal(index * 2 + 1)

    def postOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.customList[index])

    def levelOrderTraversal(self,index):
        for i in range(index, self.lastUsedIndex + 1):
            print(self.customList[i])

    def deleteNode(self,value):
        if self.lastUsedIndex == 0:
            return "Empty"
        else:
            for i in range(1, self.lastUsedIndex+1):
                if self.customList[i] == value:
                    self.customList[i] = self.customList[self.lastUsedIndex]
                    self.customList[self.lastUsedIndex] = None
                    self.lastUsedIndex -= 1
                    return "Deleted the node"
                
    def delete(self):
        self.customList = None
        return "Deleted the entire BT!!"
            

newBT = BinaryTree(8)
print(newBT.insert('Drinks'))
print(newBT.insert('Hot'))
print(newBT.insert('Cold'))
