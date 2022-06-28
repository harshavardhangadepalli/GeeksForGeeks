class Solution:
    def count(self, S, m, n):
        dp = dict()
        S.sort()
        def recursion(val,i):
            if (val,i) in dp:
                return dp[(val,i)]
            if val == 0:
                dp[(val,i)] = 1
                return dp[(val,i)]
            if val < 0:
                dp[(val,i)] = 0
                return dp[(val,i)]
            if i >= m and val > 0:
                dp[(val,i)] = 0
                return dp[(val,i)]
            if S[i] > val:
                return 0  
            dp[(val,i)] = recursion(val-S[i],i) + recursion(val,i+1)
            return dp[(val,i)]
        return recursion(n,0)
Solution().count([1,2,3],3,5)