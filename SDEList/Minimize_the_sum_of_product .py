class Solution:
    def minValue(self, a, b, n):
        # Your code goes here
        a.sort(reverse=True)
        b.sort()
        summer = 0
        for i in range(n):
            summer += a[i] * b[i]
        return(summer)

print(Solution().minValue([6,1,9,5,4],[3,4,8,2,4],5))