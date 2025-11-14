## Interview prep questions for Stack

## Describe how will you use a single python list to implement 3 stacks

## stack [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ]
## stack 1 : [0 , 1 , 2]  --> [0, n/3]
## stack 2 : [3 , 4 , 5]  --> [n/3 , 2n/3]
## stack 3 : [6 , 7 , 8]  --> [2n/3, n]
## Soln -->

class MultiStack:
    def __init__(self,stackSize):
        self.numberOfStacks = 3
        self.custList = [0] * (stackSize * self.numberOfStacks)   ## [0, 0 , 0 , 0 , 0 , 0, 0, 0 ,0]
        self.sizes = [0] * self.numberOfStacks   ## for a particular stack --> [0 0 0], if Stack 2 has 2 items, sizes will be [0, 2, 0].
        self.stackSize = stackSize    ### we decide the stacksize at the start by inserting it, saves the limit of each stack 


    def isFull(self,stackNumber):
        if self.sizes[stackNumber] == self.stackSize:
            return True
        else:
            return False
        
    def isEmpty(self,stackNumber):
        if self.sizes[stackNumber] == None:
            return True
        else:
            return False
        
    def indexOfTop(self,stackNumber):
        offset = stackNumber * self.stackSize
        return offset + self.sizes[stackNumber] - 1

    def push(self,item, stackNumber):
        if self.isFull(stackNumber):
            return "Stack is Full"
        else:
            self.sizes[stackNumber] += 1
            self.custList[self.indexOfTop(stackNumber)] = item

    def pop(self,stackNumber):
        if self.isEmpty(stackNumber):
            return "The stack is empty"
        else:
            value = self.custList[self.indexOfTop(stackNumber)]
            self.custList[self.indexOfTop(stackNumber)] = 0
            self.sizes[stackNumber] -= 1
            return value
        
    def peek(self,stackNumber):
        if self.isEmpty(stackNumber):
            return "The stack is empty"
        else:
            value = self.custList[self.indexOfTop(stackNumber)]
            return value





