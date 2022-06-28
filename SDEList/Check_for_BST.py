class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        l = list()
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            l.append(root.data)
            traversal(root.right)
        traversal(root)
        l_new = l[::]
        l_new.sort()
        if l == l_new:
            return True
        return False