#CONVERSION OF ARRAY INTO LINKEDLIST
class Node :
    def __init__ (self,data):
        self.data = data 
        self.next = None 
class LinkedList :
    def __init__ (self,head ):
        self.head = None 
    def ArrToLL (self, arr):
        for data in arr:
            new_node = Node (data)
            last = new_node 
            
            if self.head is None:
                self.head = new_node
                last = new_node 
            else:
                last.next = new_node 
                last = new_node     
#CONVERSION OF ARRAY INTO DOUBLY LINKEDLIST
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None 
class DoublyLinkedList:
    def __init__(self, head):
        self.head = None 
    def ArrToDll (self , head):
        for data in arr:
            new_node = Node(arr[0])
            if self.head is None:
                self.head = new_node 
                last = new_node    #track the last node added
            else:
                last.next = new_node
                new_node.prev = last 
                last = new_node   
                
            