class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        curr_prefix = arr[0]
        for i in range(len(arr)):
            j = 0
            k = 0
            while True:
                if j >= len(curr_prefix):
                    # curr prefix  will remain
                    break
                if k >= len(arr[i]):
                    # curr prefix will become the arr[i]
                    curr_prefix = arr[i]
                    break
                if curr_prefix[j] != arr[i][k]:
                    if j== 0 or k == 0:
                        return -1
                    curr_prefix = curr_prefix[:j]
                    break
                j += 1
                k += 1
        return curr_prefix

print(Solution().longestCommonPrefix(['abcd','bc','abb','ab','b'],5))