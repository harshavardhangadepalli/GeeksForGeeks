class Node:
    def __init__(self,val=0):
        self.next = None
        self.prev = None
        self.val = val
class MyStack:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
    #Function to push an integer into the stack.
    def push(self, data):
        # Add code here
        n = Node(data)
        self.tail.prev.next = n
        n.next = self.tail
        n.prev = self.tail.prev
        self.tail.prev = n


    #Function to remove an item from top of the stack.
    def pop(self):
        # Add code here
        if self.tail.prev == self.head:
            return -1
        n = self.tail.prev
        self.tail.prev = n.prev
        n.prev.next = self.tail
        return n.val