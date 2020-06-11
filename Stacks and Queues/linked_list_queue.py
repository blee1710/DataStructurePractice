# Queue implementation using a linked list

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None 
        self.last = None 
        self.length = 0
    
    def peek(self):
        if self.length == 0:
            return None 
        
        else:
            return self.first
    
    def enqueue(self, value):
        toAdd = Node(value)
        if self.length == 0:
            self.first = toAdd 
            self.last = toAdd
        
        else: 
            self.last.next = toAdd 
            self.last = toAdd
        
        self.length += 1 

        return self 

    def dequeue(self):
        if self.length == 0:
            return None 
        
        else:
            temp = self.first
            if self.first == self.last:
                self.last = None
            self.first = temp.next
            self.length -= 1 

            #return temp
        
        return self

myQueue = Queue() 
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)

print(myQueue.peek().data)
myQueue.dequeue()
print(myQueue.peek().data)
myQueue.dequeue()
print(myQueue.peek().data)
myQueue.dequeue()
print(myQueue.peek())
