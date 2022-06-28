'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
#Function to serialize a tree and return a list containing nodes of tree.
def serialize(root, A):
    #code here
    def recursion(node):
        if not node:
            A.append(-1)
            return
        A.append(node.data)
        recursion(node.left)
        recursion(node.right)
    recursion(root)
    return A
#Function to deserialize a list and construct the tree.   
idx = 0
def deSerialize(A):
    global idx
    def recursion():
        global idx
        if idx>=len(A):
            return None
        if A[idx] == -1:
            return None
        temp = Node(A[idx])
        idx+=1
        temp.left = recursion()
        idx+=1
        temp.right = recursion()
        return temp
    return recursion()

_1 = Node(20)
_2 = Node(8)
_3 = Node(22)
_1.left = _2
_1.right = _3


# _1 = Node(1)
# _2 = Node(2)
# _3 = Node(3)
# _4 = Node(4)
# _5 = Node(5)
# #root will be _1
# _1.left = _2
# _2.left =_3
# _2.right = _4
# _1.right = _5
A = serialize(_1,[])
print(serialize(deSerialize(A),[]))
