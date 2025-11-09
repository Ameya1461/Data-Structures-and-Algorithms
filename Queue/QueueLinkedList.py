# Implementation of Queue --> LinkedList 
# Operations --> Enqueue, Dequeue, Peek, Empty, Delete (no full, since no capacity)

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
class Linkedlist:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

class Queue:
    def __init__(self):
        self.linkedlist = Linkedlist()  # Calling the object for LL with head and tail

    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return ' '.join(values)
    
    def enqueue(self,value):
        new_node = Node(value)
        if self.linkedlist.head == None:
            self.linkedlist.head = new_node
            self.linkedlist.tail = new_node
        else:
            self.linkedlist.tail.next = new_node
            self.linkedlist.tail = new_node

    def isEmpty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            current = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = current.next 
        return current
    
    def peek(self):
        if self.isEmpty():
            return "Queue Empty!!"
        else:
            return self.linkedlist.head
        
    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None

customQueue = Queue()
customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)
print(customQueue)
print(customQueue.dequeue())
print(customQueue)

        

        