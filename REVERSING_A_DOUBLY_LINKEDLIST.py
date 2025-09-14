class Node:
    def __init__(self, data, next_node=None, back_node=None):
        self.data = data
        self.next = next_node
        self.back = back_node
class DoublyLinkedlist:
    def __init__(self,head):
        self.head = None 
    def revAdll (self):
        new_node = Node(data)
        last = new_node 
        current = self.head
        
        while current.next:
            current = current.next 
        '''last = current.prev        # last idhar ek variable hai jisko temporary bol skte h jo swaping me help kr rah h 
        current.prev = current.next 
        current.next = last 
        current = current.prev ''' 
        current.next, current.prev = current.prev, current.next 
        # both way are correct which helps in swapping 
        