# Singly Linked List
# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# class LinkedList:

#     def __init__(self,value):
#         new_node = Node(value)   
#         self.head = new_node  
#         self.tail = new_node
#         self.length = 1

# # new obj
# new_linked_list = LinkedList(10)
# print(new_linked_list.head)

################################################
## APPEND METHOD -- INSERT AT THE END  ##

# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def __str__(self):
#         temp_node = self.head
#         result = ' '
#         while temp_node is not None:
#             result += str(temp_node.value)
#             if temp_node.next is not None:
#                 result += ' --> '
#             temp_node = temp_node.next
#         return result

#     def append(self,value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1

# result = LinkedList()
# result.append(10)
# result.append(20)
# result.append(30)
# print(result)


#################
## PREPAND METHOD -- INSERT AT THE START   ##

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepand(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node 
        self.length += 1

    def __str__(self):
        temp_node = self.head
        result = ' '
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

new_linked_list = LinkedList()
new_linked_list.prepand(2)
new_linked_list.prepand(25)
new_linked_list.prepand(29)   
print(new_linked_list)


##### INSERT METHOD -- AT SPECIFIC / ANY POSITION IN LINKED LIST #####

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # INSERT METHOD
    def insert(self,index, value):
        new_node = Node(value)
        if index < 0 and index > self.length:
            return False
        elif self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:   
            temp_node = self.head
            for _ in range(index - 1):    #### 0(n)
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True


############ Traverse in a single linked list #############

    def traverse(self):
        current = self.head 
        while current is not None:
            print(current.value)
            current = current.next

############ Search method of a specific value #############
    def search(self,target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
        return False


################ GET METHOD ###################################
    def get(self,index):
        if index == -1:
            return self.tail.value
        if index < -1 or index >= self.length:
            return False
        current = self.head
        for _ in range(index):
            current = current.next
        return current

###################### SET METHOD ############################

    def set(self,index,value):
        # if index == -1:
        #     self.tail.value = value
        #     return value
        # if index < -1 or index > self.length:
        #     return None
        # current = self.head
        # for _ in range(index):
        #     current = current.next
        # current.value = value
        # return value
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False


##################  POP FIRST ######################

    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node


######## Pop Method (last element) ###########

    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head =None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node
    

######### Remove method ###############
    def remove(self,index):
        if index >= self.length or index < -1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1 or index == -1:
            return self.pop()
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node


############# Delete all ###########

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

#############################################################################################################