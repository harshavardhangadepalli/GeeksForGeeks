class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        dp = [0] * len(arr)
        dp[0] = arr[0]
        for i in range(1,len(arr)):
            if arr[i] < arr[i] + dp[i-1]:
                dp[i] = arr[i] + dp[i-1]
            else:
                dp[i] = arr[i]
        return max(dp)

print(Solution().maxSubArraySum([1,2,3],3))