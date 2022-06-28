class Solution:
    #Function to return maximum path sum from any node in a tree.
    def __init__(self):
        self.maxx = -2**32
    def findMaxSum(self, root): 
        #Your code here
        # max of a node = max(left,right)
        # if left or right doesn't exist, max(node) = val(node)
        def recursion(node):
            # if left node, return the value of leaf node
            if not node:
                return -2**32
            if not node.left and not node.right:
                self.maxx = max(node.data,self.maxx)
                return node.data
            left = recursion(node.left)
            right = recursion(node.right)
            self.maxx = max(self.maxx, node.data)
            if node.left:
                self.maxx = max(self.maxx, node.data+left)
            if node.right:
                self.maxx = max(self.maxx, node.data+right)
            if node.left and node.right:
                self.maxx = max(self.maxx, node.data+left+right)
            return max(node.data, node.data+left, node.data+right)
        recursion(root)
        return self.maxx