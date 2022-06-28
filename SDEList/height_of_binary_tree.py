class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        self.ans=-1
        def solve(root):
            if not root:
                return 0
            if not root.left and not root.right:
                self.ans=max(self.ans, 1)
                return 1
            left=solve(root.left)
            right=solve(root.right)
            self.ans=max(self.ans, max(left, right)+1)
            return max(left, right)+1
        solve(root)
        return self.ans