class Solution_dp:
    def minJumps(self, arr, n):
        dp = [10**7+1 for i in range(n)]
        
        def solve(i):
            if i >= n - 1:
                return 0
            if dp[i] != (10**7+1):
                return dp[i]
            for j in range(1,arr[i]+1):
                dp[i] = min(dp[i], 1 + solve(i+j))
            return dp[i]
        return solve(0)

class Solution:
    def minJumps(self, arr, n):
        maxReachable = 0
        last_pos = 0
        jumps = 0
        i = 0
        while last_pos < n-1:
            maxReachable = max(maxReachable, i+arr[i])
            if i == last_pos:
                last_pos = maxReachable
                jumps += 1
            i += 1
        return jumps
            
            