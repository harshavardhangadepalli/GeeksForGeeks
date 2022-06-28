class Solution:
    def trappingWater(self, arr,n):
        #Code here
        # use two arrays to store left maximum and right maaximum for any given element at i
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = arr[0]
        right_max[n-1] = arr[n-1]
        for i in range(1,n):
            left_max[i] = max(left_max[i-1],arr[i])
        for i in range(0,n-1)[::-1]:
            right_max[i] = max(right_max[i+1],arr[i])
        s = 0
        for i in range(n):
            # calculating water above each block
            s += min(right_max[i], left_max[i]) - arr[i]
        return s