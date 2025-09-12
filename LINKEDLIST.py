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
                   