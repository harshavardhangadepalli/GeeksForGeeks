class Solution:
    def firstElementKTime(self,  a, n, k):
        # code here
        d = dict()
        if k == 1:
            return a[0]
        for item in a:
            if item not in d:
                d[item] = 1
                continue
            d[item] += 1
            if d[item] >= k:
                return item

print(Solution().firstElementKTime([3,1,2],3,1))