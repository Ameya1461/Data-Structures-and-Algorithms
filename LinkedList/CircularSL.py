class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CSLinkedList:
    # def __init__ (self,value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

    # In case of empty SinglyCLL
    def __init__(self):
        self.head= None
        self.tail = None
        self.length = 0

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

    # Append(at end) Method of Singly circular linkedlist
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        self.length += 1

    # Prepand method
    def prepand(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insert(self,value,index):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.length += 1

    def traversal(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next
            if curr == self.head:
                break

    def search(self,target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break
        return False
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current 

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
        elif self.length == 1:
            self.head = None
            self.tail = None
            return popped_node
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node

    # IMPORTANT : SEE THE LOGIC    
    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            return popped_node
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:   # STOP IT AT THE 2ND LAST NODE
                temp_node = temp_node.next
            self.tail = temp_node
            self.tail.next = self.head
            popped_node.next = None
        self.length -=1
        return popped_node
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            prev_node = self.get(index - 1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
        self.length -= 1
        return popped_node
        # temp = self.head
        # while temp:
        #     for _ in range(index - 1):
        #         temp = temp.next
        #     temp.next = temp.next.next
        #     temp.next.next = None
        #     self.length -= 1
        #     return temp
        # return False

    def delete_all(self):
        if self.tail:
            self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0
            
csLinkedList = CSLinkedList()
csLinkedList.append(20)
csLinkedList.append(30)
csLinkedList.prepand(5)
csLinkedList.prepand(6)
print(csLinkedList)
# csLinkedList.insert(50,0)
# print(csLinkedList)
# print(csLinkedList.search(50))
# print(csLinkedList.pop())
print(csLinkedList.remove(2))
print(csLinkedList)