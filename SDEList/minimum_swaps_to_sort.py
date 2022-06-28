class Solution:
    #Function to find the minimum number of swaps required to sort the array.
    def __init__(self):
        self.count = 0
    def minSwaps(self, nums):
        #Code here
        a = nums[::]
        a.sort()
        d = dict()
        for i in range(len(a)):
            d[a[i]] = i
        swaps = 0
        def helper(nums):
            has_swapped = False
            for i in range(len(nums)):
                if i != d[nums[i]]:
                    # we need to swap item at index i with item at index d[nums[i]]
                    nums = swap(nums,i,d[nums[i]])
                    self.count+=1
                    has_swapped = True
            return has_swapped
        def swap(nums,i1,i2):
            temp = nums[i1]
            nums[i1] = nums[i2]
            nums[i2] = temp
            return nums
        while(helper(nums)):
            continue
        return self.count

print(Solution().minSwaps([10,19,6,3,5]))