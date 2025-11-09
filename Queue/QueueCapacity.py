## Implementation of Queue with fixed size (Circular Queue)

class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]  # Since we want to have an empty list of a fixed size
        self.maxSize = maxSize
        self.top = -1
        self.start = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        if self.start == 0 and self.top + 1 == self.maxSize:
            return True
        elif self.top + 1 == self.start:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def enqueue(self,value):
        if self.isFull():
            return "The Queue is Full"
        if self.top + 1 == self.maxSize:  ## pointer reached end of array, not that the queue is logically full yet
            self.top = 0
        else:
            self.top += 1
        if self.start == -1:
            self.start = 0
        self.items[self.top] = value
        return "The element is inserted at the end of the Queue!!"
        
    # def dequeue(self):

        
        
customQueue = Queue(3)
customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)
print(customQueue.enqueue(40))
print(customQueue)

