class Solution:
    def nextLargerElement(self,arr,n):
        stack = list()
        new_arr = list()
        new_arr.append(-1)
        stack.append(arr[-1])
        for i in range(n-2,-1,-1):
            print(arr[i])
            print(stack)
            while len(stack)!=0:
                if stack[-1] > arr[i]:
                    new_arr.append(stack[-1])
                    stack.append(arr[i])
                    break
                else:
                    stack.pop()
            if len(stack)==0:
                new_arr.append(-1)
                stack.append(arr[i])
        return(new_arr[::-1])

Solution().nextLargerElement([1,3,2,4],4)