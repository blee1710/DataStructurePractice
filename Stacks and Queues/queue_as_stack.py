# Implementation of a queue as a stack(using array implementation) 

class StackQueue:
    def __init__(self):
        self.inStack = [] 
        self.outStack = [] 
    
    #moves elements from instack when outstack has no elements
    def shift(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())

    def enqueue(self, value):
        self.inStack.append(value)

    def dequeue(self):
        self.shift()
        self.outStack.pop()
    
    def peek(self):
        self.shift()
        return self.outStack[-1]

myQueue = StackQueue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print(myQueue.peek())
myQueue.dequeue()
print(myQueue.peek())
myQueue.dequeue()
print(myQueue.peek())
myQueue.dequeue()