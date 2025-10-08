# IMPLEMENTATION OF STACK USING ARRAY
class Stack:
    def __init__(self,size):
        self.size = size 
        self.top = -1
        self.stack = [None] * size
    def isEmpty(self):
        if self.top == -1:
            print("stack is empty")
            return None 
    def isFull(self):
        if self.top == size - 1 :
            print("stack overflow")
            return None 
    def push(self, data):
        if isFull():
            print("stack overflow")
            return 
        top += 1 
        self.stack[self.top] = data 
        print (f"{data} has been pushed")
    def pop(self):
        if self.top == -1:
            print("stack is empty")
            return None 
        popped = self.stack[self.top] 
        self.top -= 1 
        return popped 
    def seek(self):
        if isEmpty():
            print("stack is empty")
            return None 
        return self.stack[self.top]
    def display(self):
        if isEmpty():
            print("stack is empty")
            return None 
        print("STACK : ", self.stack[:self.top + 1 ])
        
# IMPLEMENTATION OF STACK USING LINKEDLIST 
class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
class StackLL:
    def __init__(self):
        self.top = None 
    def isEmpty(self):
        return self.top is None 
    def push (self,data):
        new_node = Node(data)
        new_node.next = self.top 
        self.top = new_node 
        print("inserted")
    def pop(self):
        if isEmpty():
            return None 
        popped = self.top 
        self.top = self.top.next 
        return popped 
    def peek(self):
        if isEmpty():
            return None 
        return self.stack[self.top]
    def display(self):
        if isEmpty():
            return None 
        temp = self.top 
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next 
        print(result)
        
# IMPLEMENTATION OF STACK USING QUEUE 
'''1.) PUSH COSTLY APPROACH'''
from QUEUE import Queue 
class stackUsingQueue:
    def __init__(self):
        self.q = Queue()
    def push(self,x):
        size = self.q.qsize()
        self.q.put(x)
        for _ in range(size):
            self.q.put(self.q.get())
    def pop(self):
        if self.empty():
            return None 
        return self.q.get()
    def top(self):
        if self.empty():
            return None 
        return self.q.queue[0]
    def empty(self):
        return self.q.empty         
    
'''2.) POP COSTLY APPROACH''' 
from Queue  import Queue
class stackUsingQueue:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    def push(self,x):
        self.q1.put(x)
    def pop(self):
        size = self.q1.q1size()
        if empty():
            return self.empty()
        while size > 1:
            self.q2.put(self.q1.get())
        popped = self.q1.get()
        self.q1 , self.q2 = self.q2 , self.q1 
        return popped 
    def peek(self):
        if empty():
            return self.empty()
        while size > 1:
            self.q2.put(self.q1.get())
        top_elem = self.q1.get()
        self.q1 , self.q2 = self.q2 , self.q1 
        return top_elem 
    def empty(self):
        return self.q1.empty()
         
        
'''INFIX : A + B
   POSTFIX : AB+ 
   PREFIX : + AB'''  

# INFIX TO POSTFIX 

def infixToPost(expression):
    precedence = {'^': 3, '*': 2, '/':2, '+': 1, '-': 1}
    stack = []
    result = ' '
    
    for char in expression:
        if isalnum():
            result += char
        elif char = '(':
            stack.append(char)
        elif char = ')':
            while stack and stack[-1]!= '(':
                result += char 
        stack.pop()
        else:
            while stack and stack[-1]!= '(' and precedence.get(char,0) <= precedence.get(stack[-1],0):
                result += stack.pop()
            stack.append(char)
    while stack:
        result += char 
    return result 
                
# INFIX TO PREFIX 
'''1) reverse the given string 
   2) then change the '(' with this ')' and vice versa
   3) convert the infix to postfix
   4) then output which is generated is display in reverse manner '''
   
def infixToPostfix(exprssion):
    precedence = {'^':3,'*':2,'/':2,'+':1,'-':1}
    expression = exprssion[::-1]
    reversed_expression = ' '
    result = ' ' 
    stack = []
    for char in expression:
        if char = '(':
            reversed_expression += ')'
        elif char = ')':
            reversed_expression += '('
        else:
            reversed_expression += char 
    expression = reversed_expression 
    for char in expression:
        if isalnum():
            result += char
        elif char = ' (':
            stack.append(char )
        elif char = ')':
            while stack and stack[-1]!= '(':
                result += char 
            stack.pop()
        else:
            while (stack and stack[-1]!='(' and precedence.get(char,0) <= precedence.get(stack[-1],0)):
                result += char 
            stack.append(char)
    while stack:
        result += char
    return result[::-1]            
            
        
            
             