# Circular Doubly Linkedlist

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

    
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # def __init__(self,value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     new_node.prev = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

    def __str__(self):
        temp = self.head
        result = ''
        while temp:
            result += str(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            result += ' -> '
        return result

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length += 1

    def prepand(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.tail.next = new_node
            new_node.prev = self.tail
            self.head = new_node
        self.length += 1

    def insert(self,index,value):
        new_node = Node(value)
        if index == self.length:
            return self.append(index)
        elif index == 0:
            return self.prepand(index)
        elif index < 0 or index > self.length:
            return None
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        new_node.next = temp.next
        new_node.prev = temp
        temp.next = new_node
        new_node.next.prev = new_node
        self.length += 1

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            if temp == self.head:
                break
    def reverse(self):
        temp= self.tail
        while temp:
            print(temp.value)
            temp = temp.prev
            if temp == self.tail:
                break

    def search(self,target):
        temp = self.head
        while temp:
            if temp.value == target:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    def get(self,index):
        if index == -1:
            return self.tail.value
        elif index < -1 or index >= self.length:
            return False
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            return popped_node
        else:
            self.tail.next = popped_node.next
            popped_node.next.prev = self.tail
            self.head = popped_node.next
            popped_node.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        # better method is to point the popped node/ temp to tail as we have previous in doubly
        temp = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            return temp
        else:
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail.prev = None
            self.tail.next = None
            self.head.prev = temp
            self.tail = temp
        self.length -= 1
        return temp
    
    def remove(self,index):
        if index == 0:
            return self.pop_first()
        elif index == self.length:
            return self.pop()
        elif index > self.length or index < 0:
            return None
        previous_node = self.get(index - 1)
        popped_node = previous_node.next
        previous_node.next = popped_node.next
        popped_node.prev = None
        popped_node.next.prev = previous_node
        popped_node.next = None
        self.length -=1
        return popped_node



        
cdll = CircularDoublyLinkedList()
# print(cdll)
cdll.append(30)
cdll.append(10)
cdll.append(20)
print(cdll)
cdll.prepand(4)
cdll.prepand(6)
print(cdll)
cdll.insert(2,7)
print(cdll)
cdll.insert(6,22)
print(cdll)
cdll.insert(7, 29)
print(cdll)
# print(cdll.reverse())
# print(cdll.search(7))
cdll.pop_first()
print(cdll)
cdll.pop()
print(cdll)
cdll.remove(2)
print(cdll)