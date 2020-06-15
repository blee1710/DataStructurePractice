# Implementation of a binary search tree ... not so fun

class Node:
    def __init__(self, data = None):
        self.left = None
        self.right = None 
        self.data = data


class BinarySearchTree:
    def __init__(self):
        self.root = None 
    
    def insert(self, data):
        toAdd = Node(data)

        if self.root == None:
            self.root = toAdd 
            return self 
        else: 
            curr = self.root 
            while True:
                # going right
                if toAdd.data > curr.data:
                    if curr.right != None:
                        curr = curr.right 
                    else: 
                        curr.right = toAdd
                        return self
                # going left
                else:
                    if curr.left != None:
                        curr = curr.left 
                    else: 
                        curr.left = toAdd
                        return self
            
    def lookup(self, data):
        curr = self.root 
        while curr != None:
            if data < curr.data:
                curr = curr.left 
            elif data > curr.data: 
                curr = curr.right 
            elif data == curr.data: 
                return curr 
        
        return False
    
    def remove(self, data):
        curr = self.root
        parent = None
        while curr != None:
            if data < curr.data:
                parent = curr 
                curr = curr.left

            elif data > curr.data:
                parent = curr 
                curr = curr.right

            elif data == curr.data:
                # match

                # scenario 1 - no child to the right
                if curr.right == None:
                    if parent == None:
                        self.root = curr.left 
                    else: 
                        # parent > curr, curr.left becomes child of parent 
                        if curr.data < parent.data:
                            parent.left = curr.left

                        elif curr.data > parent.data:
                            parent.right = curr.left
                # scenario 2 - right child with no left child
                elif curr.right.left == None:
                    if parent == None:
                        self.root = curr.left
                    else:
                        curr.right.left = curr.left

                        # if parent > curr, right child of left becomes parent
                        if curr.data < parent.data:
                            parent.left = curr.right 

                        # if parent < curr, right child becomes right child of parent
                        elif curr.data > parent.data:
                            parent.right = curr.right
                # scenario 3 - right child with a left child
                else:
                    # get right child's leftmost child 
                    leftmost = curr.right.left 
                    leftmostParent = curr.right 
                    while leftmost.left != None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left
                    
                    # parent left subtree is now leftmost.right subtree 
                    leftmostParent.left = leftmost.right 
                    leftmost.left = curr.left 
                    leftmost.right = curr.right

                    if parent == None:
                        self.root = leftmost 
                    else:
                        if curr.data < parent.data:
                            parent.left = leftmost
                        elif curr.data > parent.data:
                            parent.right = leftmost 
                    
                return True
                         
        return False 

tree = BinarySearchTree()

tree.insert(1)
tree.insert(2)
tree.insert(5)
tree.insert(3)

print(tree.lookup(3)) # returns node 
print(tree.remove(3)) # True 
print(tree.lookup(3)) # False 
print(tree.lookup(7)) # False