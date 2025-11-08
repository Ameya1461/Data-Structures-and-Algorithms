# Stack Implementation using list/array
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def __str__(self):
        if self.isEmpty():
            return "stack is empty"
        values = [str(x) for x in reversed(self.items)]
        return '\n'.join(values)
    
    def push(self,element):
        self.items.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.items.pop()
    
    def peek(self):
        if self.isEmpty():
            return "stack empty"
        return self.items[-1]
    
    def size(self):
        return len(self.items)  
    
    def clear(self):
        self.items = [] # empty list



mystack = Stack()
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.pop()
print(mystack)
mystack.push(30)
print(mystack)