class Solution:
    # return true/false denoting whether the tree is Symmetric or not
    def isSymmetric(self, root):
        self.flag = True
        def recursion(root1,root2):
            if self.flag == False:
                return
            if not root1 and not root2:
                return
            if root1 and root2:
                if root1.data == root2.data:
                    recursion(root1.left,root2.right) 
                    recursion(root1.right,root2.left)
                    return
                self.flag = False
                return
            self.flag = False
            return
        recursion(root,root)
        return self.flag