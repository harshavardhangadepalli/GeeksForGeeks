class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        dp = [0] * N
        dp[0] = arr[0]
        for i in range(1,N):
            if arr[i] < dp[i-1] + arr[i]:
                dp[i] = arr[i] + dp[i-1]
                continue
            dp[i] = arr[i]
        print(dp)

Solution().maxSubArraySum([1,2,3,-2,5],5)