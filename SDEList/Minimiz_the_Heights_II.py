# something wrong with the problem?


class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        # initially, the highest would be arr[n-1] and arr[0] respectively
        high = arr[n-1] - k
        low = arr[0] + k
        gap = arr[n-1] - arr[0]
        for i in range(n):
            if i + 1 >= n:
                break
            high = max(arr[n-1]-k, arr[i]+k)
            low = min(arr[0]+k, arr[i+1]-k)
            gap = min(gap,high-low)
        return gap

Solution().getMinDiff([1,5,8,10],4,2)