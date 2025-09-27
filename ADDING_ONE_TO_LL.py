class Node :
    def __init__(self,next = None, data):
        self.next = next  
        self.data = data 
class Solution (object):
    def reverseLinkedList (self, head):
        temp = head 
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev 
            prev = temp 
            temp = front
    def addOne (self,head):
            head = self.reverseLinkedList (head)
            temp = head 
            carry = 1 
            
            while temp is not None:
                temp.data = temp.data + carry 
                if temp.data < 10:
                    carry = 0 
                    break
                else:
                    temp.data = 0  
                    carry = 1
            temp = temp.next 
            if  carry == 1 :
                new_node = Node (1)
                head = self.reverseLinkedList(head)
                new_node.next = head 
                return new_node
            head = self.reverseLinkedList(head)
            return head   

  