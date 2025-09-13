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
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

#DELETION AT Kth POSITION  

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
            if current is None or current.next is None:
                return
            current = current.next
        
        node_to_delete = current.next
        if node_to_delete is None:     #  agar position invalid hai
            print("Position out of range")
            return
        
        #  update links to bypass the node to delete
        current.next = node_to_delete.next
        if node_to_delete.next:       #  agar node to delete last nahi hai
            node_to_delete.next.prev = current

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
             