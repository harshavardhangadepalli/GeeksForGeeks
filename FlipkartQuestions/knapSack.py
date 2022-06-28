# User function Template for python3

class Solution:
    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        dp = dict()
        def recursion(index,total_weight):
            if index == n:
                return -1
            if total_weight > W:
                return -1
            if index in dp:
                return dp[index]
            include = val[index] + recursion(index+1,total_weight+wt[index])
            exclude = recursion(index+1,total_weight)
            dp[index] = max(include,exclude)
            return dp[index]
        recursion(0,0)
        print(dp)
        if dp[0] < 0:
            return 0
        return dp[0]


print(Solution().knapSack(4, [4,5,1], [1,2,3], 3))
