class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        s1 = set(a)
        s2 = set(b)
        diff = abs(sum(a) - sum(b))
        if sum(a) > sum(b):
            