#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printBoundaryView(self, root):
        # Code here
        left_nodes = list()
        right_nodes = list()
        leaves = list()
        def left_finder(node):
            if not node:
                return
            while node:
                left_nodes.append(node.data)
                if not node.left:
                    if node.right:
                        node = node.right
                    else:
                        break
                else:
                    node = node.left
        def right_finder(node):
            if not node:
                return
            while node:
                right_nodes.append(node.data)
                if not node.right:
                    if node.left:
                        node = node.left
                    else:
                        break
                else:
                    node = node.right
        def leaf_finder(node):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.data)
                return
            leaf_finder(node.left)
            leaf_finder(node.right)
        if not root:
            return None
        if not root.left and not root.right:
            # this means that there is only root
            return root.data
        left_finder(root.left)
        right_finder(root.right)
        leaf_finder(root)
        r = right_nodes[::-1]
        new_list = [root.data] + left_nodes[:len(left_nodes)-1] + leaves + r[1:]
        return new_list
        