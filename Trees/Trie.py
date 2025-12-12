# Implementation of Trie DS --> Used to store or search a new string in a time and efficient way

# Creating of a Trie --> O(1), O(1)
class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):  # O(M) both --> M is the length of string
        currentNode = self.root 
        for char in word:
            newNode = currentNode.children.get(char)  ## Check if this character already exists as a child of the current node
            if newNode == None:   # If the char does not exist
                newNode = TrieNode()  # Create a new node
                currentNode.children.update({char:newNode})   # assign/update/add/insert that char to the node
            currentNode = newNode   # Move current to the child node so you can continue inserting the next character.(for next interation current is at char C in case we take CAT to insert)
        currentNode.endOfString = True 
        return "Inserted Successfully!!"
     
    def searchString(self, word):  # O(M) , O(1)   ...M is the length of string
        currentNode = self.root
        for char in word:
            newNode = currentNode.children.get(char)  
            if newNode == None:
                return False
            currentNode = newNode
        
        if currentNode.endOfString == True:
            return True
        else:
            return False
            
        

newTrie = Trie()
