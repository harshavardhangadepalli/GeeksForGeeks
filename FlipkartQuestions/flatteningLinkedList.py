#User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Node:
    def __init__(self,d):
        self.data = d
        self.next = None
        self.bottom = None
def flatten(root):
    #Your code here
    def merge(a,b):
        dummy = Node(0)
        ptr = dummy
        while a and b:
            if a.data <= b.data:
                ptr.bottom = a
                a = a.bottom
            else:
                ptr.bottom = b
                b = b.bottom
            ptr = ptr.bottom
        if not a:
            ptr.bottom = b
        if not b:
            ptr.bottom = a
        return dummy.bottom

    current_node = root
    next_node = root.next
    while next_node:
        current_node = merge(current_node,next_node)
        next_node = next_node.next
    ptr = current_node
    current_node.next = None
    return current_node

_1 = Node(5)
_2 = Node(7)
_3 = Node(8)
_4 = Node(30)
_5 = Node(10)
_6 = Node(20)
_7 = Node(19)
_8 = Node(22)
_9 = Node(28)
_10 = Node(50)

_1.bottom = _2
_2.bottom = _3
_3.bottom = _4
_1.next = _5
_5.bottom = _6
_5.next = _7
_7.bottom = _8
_7.next = _9
_8.bottom = _10
x = flatten(_1)
while x:
    print(x.data)
    x = x.bottom