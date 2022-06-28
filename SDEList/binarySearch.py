class Solution:
        def binarysearch(self, arr, n, k):
                start = 0
                end = n-1
                while start <= end:
                        mid = end + ((end-start)//2)
                        if arr[mid] == k:
                                return mid
                        elif k > arr[mid]:
                                start = mid+1
                        else:
                                end = mid-1
                return -1
Solution().binarysearch([1,4,6,90,3289,128947,2143431],7,4)