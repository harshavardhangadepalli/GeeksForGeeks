class Solution:
    def MissingNumber(self,array,n):
        # code here
        s = set(array)
        for i in range(1,n+1):
            if i not in s:
                return i