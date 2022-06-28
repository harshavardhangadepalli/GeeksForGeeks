# User function Template for python3

# design the class in the most optimal way

class Node:
    def __init__(self,key,val):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key

class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self,cap):
        #code here
        self.capacity = cap
        self.d = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        if key in self.d:
            node = self.remove(self.d[key])
            self.add(node)
            return self.d[key].val
        return -1
        
    #Function for storing key-value pair.   
    def set(self, key, value):
        #code here
        if key in self.d:
            node = self.remove(self.d[key])
            self.add(node)
            self.d[key].val = value
        else:
            if len(self.d) == self.capacity:
                self.pop()
                self.add(Node(key,value))
            else:
                self.add(Node(key,value))

    def pop(self):
        temp = self.head.next
        self.head.next = temp.next
        temp.next.prev = self.head
        self.d.pop(temp.key)
        return
    def remove(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.d.pop(node.key)
        return node
    def add(self,node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.d[node.key] = node
        return
    def printer(self):
        node = self.head.next
        while node!=self.tail:
            print(node.key,node.val)
            node = node.next


l = LRUCache(3)
l.set(1,1)
l.set(2,2)
l.set(3,3)
l.get(1)
l.get(2)
l.get(3)
l.set(4,4)
l.get(1)
l.get(2)
l.get(6)
l.get(10)
l.get(100)
l.set(2,10)
l.printer()