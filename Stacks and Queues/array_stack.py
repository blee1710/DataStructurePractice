# Stack implementation using an array

class Stack:
    def __init__(self):
        self.array = []
    
    def peek(self):
        return self.array[len(self.array)-1]
    
    def push(self, value):
        self.array.append(value)
        return self

    def pop(self):
        self.array.pop(len(self.array)-1)
        return self
    
myStack = Stack() 
myStack.push('Hello')
myStack.push('Hello1')
myStack.push('Hello2')

print(myStack.peek())