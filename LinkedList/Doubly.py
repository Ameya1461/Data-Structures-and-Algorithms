# Doubly LinkedList

class Node:

    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None   # In case of doubly linkedlist, has reference to previous node as well
    
    def __str__(self):
        return f"{self.value}"
    
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp = self.head
        result = ''
        while temp:
            result += str(temp.value)
            if temp.next:
                result += ' -> '
            temp = temp.next
        return result

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            # new_node.next = None
        self.length += 1

    def prepand(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            # new_node.prev = None
        self.length += 1

    def insert(self,index, value):
        new_node = Node(value)
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node
        self.length += 1

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        
    def reverseTraversal(self):
        current = self.tail
        while current:
            print(current.value)
            current = current.prev
        
    def search(self,target):
        temp = self.head
        while temp:
            if temp.value == target:
                return True
            temp = temp.next
        return False
    
    def get(self,index): # OPTIMAL WAY --> DIVIDE LL IN 2 PARTS
        # temp = self.head
        # for _ in range(index):
        #     temp = temp.next
        # return temp
        if index == -1:
            return self.tail.value
        if index < -1 or index >= self.length:
            return False
        if index < self.length // 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set(self,index,value):
        temp = self.get(index)
        while temp:
            temp.value = value
            return True
        return False

    def pop_first(self):
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            return temp
        elif self.length == 0:
            return None
        else:
            temp.next = self.head
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp

    def pop(self):
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            return temp
        if self.length == 0:
            return None
        else:
            temp.prev = self.tail
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def remove(self,index):
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        elif index < 0 or index > self.length:
            return None
        else:
            temp = self.get(index)
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.prev = None
            temp.next = None
        self.length -= 1
        return temp 
        

newDLL = LinkedList()
newDLL.append(20)
newDLL.append(30)
print(newDLL)
newDLL.prepand(5)
newDLL.prepand(8)
print(newDLL)
newDLL.insert(2,10)
print(newDLL)
# print(newDLL.get(2))
# print(newDLL.pop_first())
print(newDLL)
# print(newDLL.pop())
# print(newDLL)
print(newDLL.remove(3))