class Solution:
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        dep.sort()
        arr.sort()
        i = 1
        j = 0
        gap = 1
        while i < n and j < n:
            gap = max(gap,i-j)
            if arr[i] < dep[j]:
                # this means that the train has arrived before the one has left
                # i will increase, but j will stay
                i += 1
                continue
            if arr[i] >= dep[j]:
                # this means that the train has arrived after one(or more) has left.
                j += 1
        gap = max(gap,i-j)
        return gap
Solution().minimumPlatform(6,['0900', '0940', '0950', '1100', '1500', '1800'],['0910', '1200', '1120', '1130', '1900', '2000'])