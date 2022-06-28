class Solution:
    def find(self,arr,k):
        if sum(arr) < 2*k:
            return 0
        def find_partition(a):
            if len(a) <= 0:
                return list()
            s = 0
            ret = list()
            for i in range(len(a)):
                s += a[i]
                if s == k:
                    ret.append(i)
                if s > k:
                    break
            return ret
        dp = dict()
        def solve(index):
            if index in dp:
                return dp[index]
            if index == len(arr):
                return 1
            l = find_partition(arr[index:])
            ans = 0
            for item in l:
                # sum will be equal to k till the location index + item.
                # we need to call find_partition on the place index+item+1, and then solve.
                ans += solve(index+item+1)
            dp[index] = ans
            return dp[index]
        return solve(0)
Solution().find()