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
         
        
        