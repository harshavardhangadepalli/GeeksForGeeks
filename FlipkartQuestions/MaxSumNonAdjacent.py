class Solution:
    #Function to return the maximum sum of non-adjacent nodes.
    def getMaxSum(self,root):
        #code here
        dp = dict()
        def function(root,dp):
            if not root:
                return 0
            if root in dp:
                return dp[root]
            # if we include not a, we cannot include it's children
            # so we can include it's grandchildren
            # we calculate sum for both cases, for each node, and then return max of both
            excluding = function(root.left,dp) + function(root.right,dp)
            including = root.data
            if root.left:
                including += function(root.left.left,dp) + function(root.left.right,dp)
            if root.right:
                including += function(root.right.left,dp) + function(root.right.right,dp)
            dp[root] = max(excluding,including)
            return dp[root]
        s = function(root,dp)
        print(s)