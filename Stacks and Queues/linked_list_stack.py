# Stack implementation using a linked list

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0 
    
    def peek(self):
        return self.top
    
    def push(self, value):
        toAdd = Node(value)
        if self.length == 0:
            self.top = toAdd 
            self.bottom = toAdd 
        else:
            toAdd.next = self.top 
            self.top = toAdd
        
        self.length += 1 

        return self 

    def pop(self):
        if self.length == 0:
            return self 

        if self.top == self.bottom:
            self.bottom = None
        #look into garbage collection for python
        self.top = self.top.next 
        self.length -= 1

        return self
    


#Testing 
myStack = Stack()

myStack.push('Hello')
myStack.push('Hello1')
myStack.push('Hello2')
myStack.push('Hello3')

print(myStack.peek().data)
myStack.pop()
print(myStack.peek().data)
myStack.pop()
print(myStack.peek().data)
myStack.pop()
print(myStack.peek().data)
