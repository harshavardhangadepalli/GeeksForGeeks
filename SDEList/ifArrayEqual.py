class Solution:
    #Function to check if two arrays are equal or not.
        def check(self,A,B,N):
            d = dict()
            d1 = dict()
            for i in A:
                if i in d:
                    d[i]+=1
                    continue
                d[i] = 1
            for i in B:
                if i in d1:
                    d1[i]+=1
                    continue
                d1[i] = 1
            if d1 == d:
                return True
            return False
Solution().check([1,4,5,6,7],[7,6,5,1,4],5)