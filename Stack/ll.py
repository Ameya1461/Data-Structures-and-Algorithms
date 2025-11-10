# Implementation using LinkedList
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def peek(self):
        if self.length == 0:
            return None
        return self.top

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
        
    def clear(self):
        self.top = None
        self.length = 0



newStack = Stack()
newStack.push(10)
newStack.push(20)
newStack.push(30)
# print(newStack.top.value)
# print(newStack.pop().value)
print(newStack.peek().value)