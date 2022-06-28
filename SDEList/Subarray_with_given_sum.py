class Solution:
    def subArraySum(self,arr, n, s):
        head = 0
        tail = 0
        su = arr[0]
        while True:
            if su == s:
                return head+1,tail+1
            if su < s:
                if tail + 1 >= n:
                    return [-1]
                tail += 1
                su += arr[tail]
                continue
            if head + 1 >= n:
                return [-1]
            head += 1
            su -= arr[head-1]