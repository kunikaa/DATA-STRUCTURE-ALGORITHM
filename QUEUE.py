#IMPLEMENTATION OF QUEUE USING ARRAY
class Queue:
    def __init__(self,size):
        self.size = size
        self.front = -1
        self.rear = -1 
        self.queue = [None] * size 
    def isEmpty(self):
        return self.front = -1
    def isFull(self):
        return (self.rear + 1)% size == self.front 
    def enqueue(self,data):
        if isFull():
            print("queue overflow")
            return None 
        self.rear = ( self.rear + 1 )% size
        self.queue[self.rear] = data 
        print("inserted")
    def dequeue(self):
        if isEmpty():
            print("empty")
            return None 
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
        else:
            self.front = (self.front + 1)% size 
        return data 
    def peek(self):
        if isEmpty():
            print("empty")
            return None
        return self.queue[self.front]
    def display(self):
        if isEmpty():
            print("empty")
            return None
        i = self.front
        result = []
        while True:
            result.append(self.queue[i])
        if i == rear:
            break             

# IMPLEMENTATION OF QUEUE BY USING LINKEDLIST 
class Node :
    def __init__(self,data):
        self.data = data 
        self.next = None 
class QueueLL:
    def __init__(self,data):
        self.rear = self.front = None 
    def isEmpty(self) :
        if self.front is None:
            return None 
    def enqueue(self,data):
        new_node = Node(data)
        if self.rear is None :
            self.rear = self.front = new_node
            return  
        self.rear.next = new_node 
        self.rear = new_node      
    def dequeue(self):
        if isEmpty():
            return None
        data = self.front 
        self.front = self.front.next 
        if self.front is None:
            self.rear = None 
        return data 
    def peek(self):
        if isEmpty():
            return None 
        return self.front.data 
    def display(self):
        result = []
        temp = front 
        while temp:
            result.append(temp.data)
        return result 
    
# IMPLEMENTATION OF QUEUE USING STACK 
class queueUsingStack :
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push (self,x):
        self.stack1.append(x)
    def pop(self):
        if not stack2 :
            while stack2:
                self.stack2.append(self.stack1.pop())
        elif self.stack2:
            return self.stack2.pop()
        else:
            return None 
    def peek(self):
        if not stack2 :
            while stack2:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2[-1]  
        else:
            returnn None
    def empty(self):
        return not self.stack1 and not self.stack2  
            
        