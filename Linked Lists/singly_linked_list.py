#Simple implementation of a single linked list

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 0 if node is None else 1
    
    def append(self, value):
        toAdd = Node(value)
        if self.head is None:
            self.head = toAdd
            self.tail = toAdd
            self.length += 1
        else:
            self.tail.next = toAdd
            self.tail = toAdd
            self.length += 1
        return self

    def prepend(self, value):
        toAdd = Node(value)
        if self.head is None:
            self.head = toAdd
            self.tail = toAdd
            self.length += 1
        else:
            toAdd.next = self.head 
            self.head = toAdd
            self.length += 1
        return self

    def traverse(self, index):
        curr = self.head 
        for x in range(index):
                curr = curr.next

        return curr

    def insert(self, index, value):
        toAdd = Node(value)
        curr = self.head
        if index >= self.length:
            return self.append(value)
        elif index == 0:
            return self.prepend(value)
        else:
            curr = self.traverse(index-1)
            toAdd.next = curr.next 
            curr.next = toAdd
            self.length +=1
        
        return self

    
    def remove(self, index):
        #do nothing if empty
        if self.length == 0:
            return self 
        
        #delete head
        elif index == 0:
            self.head = self.head.next
            self.length -= 1
            return self
            
        #delete last if index too high
        elif index >= self.length:
            curr = self.traverse(self.length-2)
        
        else:
            curr = self.traverse(index-1)

        toDelete = curr.next
        curr.next = toDelete.next 
        self.length -= 1

        return self 

    # Reverse a Singly Linked List
    def reverse(self):
        if self.length <= 1: 
            return self
        
        first = self.head
        self.tail = self.head
        second = first.next 

        while second is not None:
            temp = second.next 
            second.next = first 
            first = second 
            second = temp
        
        self.head.next = None
        self.head = first

        return self

    



    # Print all values in linked list
    def print(self):
        curr = self.head 
        while (curr is not None):
            print(f"Node Value: {curr.data}, Next Node Value: {str(curr.next.data) if curr.next != None else 'None'}")
            curr = curr.next
        return self
    

#Testing

sLinkedList = SinglyLinkedList()
sLinkedList.append(10)

ele2 = 5
ele3 = 16

sLinkedList.append(ele2)
sLinkedList.append(ele3)
sLinkedList.insert(3,44)
sLinkedList.insert(55,74)

sLinkedList.remove(0)


sLinkedList.print()

sLinkedList.reverse()
print('REVERSE')
sLinkedList.print()