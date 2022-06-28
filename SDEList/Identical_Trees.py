class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        self.flag = True
        # Code here
        def recursion(root1,root2):
            if self.flag == False:
                return
            if not root1 and not root2:
                return
            if root1 and root2:
                if root1.data != root2.data:
                    self.flag = False
                    return
                recursion(root1.left,root2.left)
                recursion(root1.right,root2.right)
                return
            self.flag = False
        recursion(root1,root2)
        return self.flag