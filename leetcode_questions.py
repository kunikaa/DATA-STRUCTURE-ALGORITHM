#REMOVING THE Nth NODE OF THE LINKEDLIST FROM 
'''TORTOISE AND HARE ALGORITHM (SLOW AND FAST POINNTER)'''
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

# 0, 1 & 2 DATA ARRANGEMENT IN A LINKEDLIST 
'''DUMPY_NODE APPROACH '''
class Solution :
    def arrangement(self,head):
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
    
#REVERSE A LINNKEDLIST 
''' BY TWO VARIABLE''' 
class Solution :
    def reverse(self,head ):
        if not head or not head.next:
            return head 
        temp = head 
        prev = None
        while temp is not None and temp.next is not None:
            front = temp.next   #firstly store the temp.next as front 
            temp.next = prev    #now here main link changed
            prev = temp         #updation of variable occur
            temp = front        #shifting
        return prev 

#ADD TWO LINKEDLIST 
'''SIMPLY BY REVERSING THEM '''
class Solution :
    def addLL (self,head ):
        t1 = list1
        t2 = list2
        dumpy_node = Node(-1)
        temp = dumpy_node 
        carry = 0
        while t1 and t2 is not None:
            if carry != 0:
                sum = carry 
                if t1:
                    sum += t1.data 
                    t1 = t1.next 
                if t2:
                    sum += t2.data 
                    t2 = t2.next 
            new_node = Node(sum % 10)   #unit place value arrangement
            carry = sum //10            #gives carry as quotient
            current.next = new_node 
            current = current.next 
        return dumpy_node.next 
                    
#CHECKING PALINDROME OF LINKEDLIST 
'''TORTOISE AND HARE ALGORITHM (SLOW AND FAST POINNTER)'''
class Solution:
    def palindrome(self,head):
        if not head or not head.next :
            return head 
        slow = head 
        fast = head 
        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next 
        prev = None                    #code for reversing the list 
        while slow :
            front = slow.next 
            slow.next = prev 
            prev = slow 
            slow = front 
        left = head 
        right = prev 
        while right:
            if left.data!=right.data 
            return False 
        return True     
          
#   ODD AND EVEN DATA ARRANGEMENT IN A LINKDLIST 
class Solution:
    def oddAndeven(self ,head) :
        odd = head
        even = head.next 
        even_head = head.next 
        while even is not None and even.next is not None:
            odd = even.next 
            odd = odd.next 
            even = odd.next 
            even = even.next 
        odd.next = even.head 
        return head 

#FIND THE INTERSECTING POINT OF THE LINKEDLSIT 
class Solution :
    def intersecting(self,head):
        if head1 is None or head2 is None:
            return None
        t1 = head1
        t2 = head2 
        while t1!=t2:
            t1 = t1.next 
            t2 = t2.next 
        if t1==t2:
            return t1 
        if t1.next == None:
            t1 = head2
        if t2.next == None:
            t2 = head1
            
# MIDDLE OF THE LINKEDLIST 
'''TORTOISE AND HARE ALGORITHM (SLOW AND FAST POINNTER)''' 
class Solution:
    def middleOfLinkedlist(self,head):
        slow = head 
        fast = head 
        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next 
        return slow 
# DETECT THERE IS A LOOP OR A  CYCLE IN A LINKEDLIST OR NOT
'''TORTOISE AND HARE ALGORITHM (SLOW AND FAST POINNTER)''' 
class Solution :
    def detectAloop(self,head):
        slow = head 
        fast = head 
        while fast is not None and fast.next is not None:
            slow  = slow.next 
            fast = fast.next.next 
            if slow == fast :
                return True 
            return False     

# STARTING NODE OF  LOOP OR A CYCLE IN THE LINKEDLIST 
'''TORTOISE AND HARE ALGORITHM (SLOW AND FAST POINNTER)'''
class Solution:
    def startingPoint(self,head ):
        slow = head 
        fast = head 
        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast:
                slow = head 
                while slow:
                    slow = slow.next 
                    fast = fast.next 
                return slow.data 
        return None
                 
            
        