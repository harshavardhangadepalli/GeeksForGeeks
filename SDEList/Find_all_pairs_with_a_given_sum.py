class Solution:
    def allPairs(self, A, B, N, M, X):
        # Your code goes here 
        s = set(B)
        l = list()
        for item in A:
            if X-item in s:
                l.append([item,X-item])
        l.sort()
        return l