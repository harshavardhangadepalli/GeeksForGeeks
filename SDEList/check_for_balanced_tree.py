class Solution:
    def isBalanced(self,root) -> bool:
        self.ans=True
        def solve(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            left=solve(root.left)
            right=solve(root.right)
            self.ans=self.ans and abs(left-right)<=1
            return max(left, right)+1
        if not root:
            return True
        if not root.left and root.right:
            return True
        solve(root)
        return self.ans