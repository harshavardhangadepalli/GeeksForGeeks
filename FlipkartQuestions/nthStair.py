#User function Template for python3

class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        # code here
        dp = dict()
        dp[1] = 1
        dp[2] = 2
        dp[0] = 0
        def recursion(x):
            if x in dp:
                return dp[x]
            dp[x] = recursion(x-1)+recursion(x-2)
            return dp[x]
        return recursion(n)%(10**9+7)
print(Solution().countWays(84)%(10**9+7))