#INSERTION AT THE HEAD OF THE DOUBLY LINKEDLIST
class Node :
    def __init__(self, data, next, prev):
        self.data = data
        self.next = None 
        self.prev = None
class doublyLinkedList:
    def __init__ (self, head):
        self.head = None 
    def insertionAtHead ():
        new_node = Node(data)
        new_node.next = self.head 
        if self.head:                  # if head exist then -->
            self.head.prev = new_node
        self.head = new_node
        
#INSERTION AT TAIL 
class Node:
    def __init__ (self, data):
        self.data = data 
        self.next =  None    
        self.prev = None 
class doublyLinkedList :
    def __init__(self):
        self.head = None 
    def insertionAtTail (self, data):
        new_node = Node(data)
        if not self.head:           
            self.head = new_node
            return  
        current = self.head 
        while current.next :
            current = current.next 
        current.next = new_node
        new_node.prev = current

# INSERTION OF NODE AT Kth POSITION IN THE DOUBLY LINKEDLIST
class Node :
    def __init__(self, data):
        self.data = data 
        self.next = None 
        self.prev = None 
class doublyLinkedlist:
    def __init__(self):
        self.head = None 
    def insertAtKthPosition (self , data , position ):
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            if self.head:                   # head exists → update its prev
                self.head.prev = new_node
            self.head = new_node
            return
        current = self.head  
        for _ in range (position - 2):       #due to zero based indexing 
            if current is None:
                return 
            current = current.next
        new_node.next = current.next     
        new_node.prev = current
        if current.next:                    # if not inserting at the end
            current.next.prev = new_node
        current.next = new_node 

# DELETION AT HEAD        
class Node :
    def __init__(self, data, next, prev):
        self.data = data
        self.next = None 
        self.prev = None
class doublyLinkedList:
    def __init__ (self, head):
        self.head = None 
    def deletionAtHead (self):
        if not self.head :
            return 
        self.head = self.head.next
        if self.head:                    # agar next node exist karta hai to uska prev None set karo
            self.head.prev = None
        
# DELETION AT TAIL       
class Node :
    def __init__(self, data, next, prev):
        self.data = data
        self.next = None 
        self.prev = None
class doublyLinkedList:
    def __init__ (self, head):
        self.head = None 
    def deletionAtTail (self):
        if not self.head:
            return 
        if not self.head.next:
            self.head = None
            return 
        current = self.head   
        while current.next:
            current = current.next 
        current.prev. next = None 
        return self.head    
  
#DELETION AT Kth POSITION       
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def deletionAtKthPosition(self, position):
        
        if not self.head:               #  agar list empty hai
            return
        
        if position == 1:                #  agar head delete karna hai
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        
        current = self.head
        #  move to (position-1)th node
        for _ in range(position - 2):
            current = current.next
        if current.next is None:
            return 
        current.next = current.next.next 
        current.next.prev = current
        return self.head 

# DELETE ALL THE OCCURENCE OF A KEY IN DOUBLY LINKEDLIST 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Solution:
    def deleteAllTheOccurennce(self,head,target):
        temp = head 
        while temp is not None and temp.next is not None:
            if temp.data == target:
                if temp == head:
                    head = head.next 
                    if head: 
                        head.prev = None
                else :
                    if temp.prev:
                        temp.prev.next = temp.next 
                    if temp.next:
                        temp.next.prev = temp.prev 
            temp = temp.next 
        return head  
        
# FIND PAIRS WITH GIVEN SUM IN DOUBLY LINKEDLIST 
class Solution:
    def pairsOfSum(self,head ):
        if not head or not head.next:
            return None
        left = head
        right = head 
        while right :
            right = right.next
        result = []
        while left != right '''not a same node '''and left.prev != right'''both pointer should not cross''':
            sum = left.data + right.data 
            if sum == target: 
                result.append((left.data, right.data))
                left = left.next 
                right = right.next 
            elif s < target:
                left = left.next 
            else:
                right = right.prev 
        return result 
    
#REMOVES DUPLICATES FROM THE DOUBLY LINKEDLIST 
class Solution:
    def removeDuplicates(self,head):
        if not head or not head.next:
            return None 
        temp = head 
        while temp and temp.next  :
            if temp.data == temp.next.data:
                nxt = temp.next.next 
                temp.next = nxt 
                if nxt:
                    nxt.prev = temp 
            else: 
                temp = temp.next 
        return head 
    
     
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
             