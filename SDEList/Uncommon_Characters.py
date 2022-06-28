class Solution:
    def UncommonChars(self,A, B):
        #code here
        A = set(A)
        B = set(B)
        s = list()
        for item in A:
            if item not in B:
                s.append(item)
        for item in B:
            if item not in A:
                s.append(item)
        if len(s) == 0:
            return -1
        else:
            s.sort()
            ans = ''
            for item in s:
                ans += item
            return ans