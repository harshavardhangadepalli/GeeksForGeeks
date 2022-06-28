class Solution:
    def minPartition(self, N):
        # code here
        d = dict()
        for item in [2000,500,200,100,50,20,10,5,2,1]:
            d[item] = N // item
            N = N - item*d[item]
            if N <= 0:
                break
        l = list()
        for key in sorted(d.keys()):
            for i in range(d[key]):
                l.append(key)
        return l[::-1]

Solution().minPartition(4851)