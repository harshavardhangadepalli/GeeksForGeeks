#User function Template for python3

'''
@input - 
node - root node of given tree
k = distance of nodes required 

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

#Function to return count of nodes at a given distance from leaf nodes.
def printKDistantfromLeaf(root, k):
    #code here
    leaf_node = list()
    children_list = dict()
    ptr = root
    children_list[root] = list()
    parent_list = dict()
    parent_list[root] = None

    def children_finder(node):
        if not node.left and not node.right:
            #this means it is a leaf node, we need not find children
            leaf_node.append(node)
            return
        #this means that it is a parent
        if node in children_list:
            if node.left:
                children_list[node].append(node.left)
                children_finder(node.left)
            if node.right:
                children_list[node].append(node.right)
                children_finder(node.right)
        else:
            children_list[node] = list()
            if node.left:
                children_list[node].append(node.left)
                children_finder(node.left)
            if node.right:
                children_list[node].append(node.right)
                children_finder(node.right)
    def traversal(node,count):
        k = 0
        while True:
            if k == count:
                return node
            if parent_list[node] == None:
                return None
            k+=1
            node = parent_list[node]
    children_finder(ptr)
    for item in children_list:
        for thing in children_list[item]:
            parent_list[thing] = item

    # for item in parent_list:
    #     if parent_list[item]!=None:
    #         print(item.data,parent_list[item].data)
    #     else:
    #         print(item.data,None)

    s = set()
    for leaf in leaf_node:
        x = traversal(leaf,k)
        if x!=None:
            s.add(x)
    return len(s)


class Node:
    def __init__(self,val):
        self.right = None
        self.data = val
        self.left = None

_1 = Node(1)
_2 = Node(2)
_3 = Node(3)
_4 = Node(4)
_5 = Node(5)
_6 = Node(6)
_7 = Node(7)
_8 = Node(8)

_1.left = _2
_1.right = _3

_2.left = _4
_2.right = _5
_3.left = _6
_3.right = _7
_6.right = _8


print(printKDistantfromLeaf(_1,2))