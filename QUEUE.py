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
        
        
        