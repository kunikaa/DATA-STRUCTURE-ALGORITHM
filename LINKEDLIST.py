# LENGHT OF THE LINKEDLIST
class Node :
    def __init__(self , data, next = None):
        self.data = data
        self.next = next
    count = 0 
    current = head 
    while current is not None:
        current = current.next
        count +=1
    return count    

# SEARCH AN ELEMENT IN LINKEDLIST
class Node :
    def __init__(self,data, next = None):
        self.data = data
        self.next = next 
def searchInLinkedlist (head, target):
    current = head
    while current is not None:
        if target == current.data:
            return 1
        current = current.next    
    return 0    
    
# DELETION OF HEAD IN A LINKEDLIST
class Node :
    def __init__(self,data, next = None):
        self.data = data
        self.next = next 
def deleteHeadNode (self):
    self.head  = self.head.next 
    
#DELETION OF THE NODE AT A GIVEN POSTION 
class Node :
    def __init__(self,data, next = None):
        self.data = data
        self.next = next 
def deletionAtPosition (head , position ):
    if position == 0 :
        return  head.next  
    current = head 
    for _ in range (position - 1):
        current = current.next 
    current.next = current.next.next        
    return head      
# DELETION OF THE NODE BY THE VALUES
class Node :
    def __init__(self,data, next = None):
        self.data = data
        self.next = next 
def deleteNodevalue (value, head):
    if head.data == value :
        return head.next 
    current = head 
    while current and currennt.next.data != value:
        current = current.next 
    if current:
        current.next = current.next.next 
    return head

#DELETION OF NODE AT THE LAST WHICH MEANS TAIL
class Node :
    def __init__(self,data, next = None):
        self.data = data
        self.next = next 
def deleteNodeTail (head):
    if not head or not head.next:
        return 0 
    current = head 
    while current.next.next :
        current = current.next 
    current.next = None
    return head 
                   
        
        
# INSERTION OF NODE IN A LINKDLIST

# INSERTION AT HEAD
class Node :
    def __init__(self,data, next = None):
        self.data = data
        self.next = next 
def insertionAtHead (head, value):
        new_node = Node (value)
        new_node.next  = head 
        return new_node 
    
# INSERTION AT TAIL
class Node :
    def __init__(self,data, next = None):
        self.data = data
        self.next = next 
def insertionAtTail (head , value):
    new_node = Node(value)
    current = head
    while current.next:
        current = current.next 
    current.next = new_node
    return head    
                    
#INSERTION AT GIVEN POSITION 
class Node :
    def __init__(self,data, next = None):
        self.data = data
        self.next = next 
def insertionAtposition (head, value, position ):
    new_node = Node(value)
    current = head 
    for _ in range (position -1 ):
        current = current.next 
    new_node = current_next 
    current.next = new_node
    return head

#INSERTION BY VALUES
class Node :
    def __init__(self,data, next = None):
        self.data = data
        self.next = next                          
def insertionByValues (values , head):
    new_node = Node(values)
    current = head 
    while current and current.next.data != values:
        current = current.next 
    if current:
        new_node.next = current.next 
        current.next = new_node
    return head   

# ROTATE A LINKEDLIST 
class Solution:
    def rotateALinkedlist(self,head,k):
        if not head or not head.next:
            return None
        length = 0 
        tail = head 
        while tail is not None and tail.next is not None:
            length += 1 
            tail = tail.next 
        if k % length ==0 :
            return head 
        new_tail = head 
        for _ in range(length-k-1):
            new_tail = new_tail.next 
        new_head = new_tail.next 
        #connecting old tail to old head 
        tail.next = head 
        #break the circle 
        new_tail.next = None  
        return new_head       