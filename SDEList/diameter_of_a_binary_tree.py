class Solution:
    
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        self.ans=-1
        def solve(root):
            if not root:
                return 0
            if not root.left and not root.right:
                self.ans=max(self.ans, 1)
                return 1
            left=solve(root.left)
            right=solve(root.right)
            self.ans=max(self.ans, left+right+1)
            return max(left, right)+1
        solve(root)
        return self.ans