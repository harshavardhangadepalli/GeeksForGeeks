class Solution:
    def reverseInGroups(self,arr,N,K):
        l = list()
        start = 0
        end = K
        while True:
            [l.append(i) for i in arr[start:end][::-1]]
            if end+K > N:
                break
            start = end
            end = end+K
        [l.append(i) for i in arr[end::][::-1]]
        return l
Solution().reverseInGroups([1,2,3,4,5],5,3)