#REMOVING THE Nth NODE OF THE LINKEDLIST FROM 
'''BY SLOW AND FAST POINTER APPROACH '''
class Solution:
    def removeNthNode(self,head,n ):
        dumpy_node = Node(-1)
        fast = dumpy_node
        slow = dumpy_node
        for _ in range(0,n+1):
            fast = fast.next 
        while fast.next is not None:
            slow = slow.next 
            fast = fast.next 
        slow.next = slow.next.next 
        return dumpy_node.next 

#ODD AND EVEN DATA ARRANGEMENT IN A LINKEDLIST 
'''DUMPY_NODE APPROACH '''
class Solution :
    def oddAndeven(self,head):
        zeroHead = Node(-1)
        oneHead = Node(-1)
        twoHead = Node(-1)
        zero = zeroHead 
        one = oneHead 
        two = twoHead 
        temp = head 
        while temp is not None and temp.next is not None:
            if temp.data == 0:
                zero.next = temp 
                zero = temp 
            elif temp.data == 1:
                one.next = temp 
                one = temp 
            else:
                two.next = temp
                two = temp 
        temp = temp.next 
        if oneHead.next :
            zero = oneHead.next  
        else:
            zero = twoHead.next 
        one.next = twoHead.next 
        two.next = None
        return zeroHead 
        