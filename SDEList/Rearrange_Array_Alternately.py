class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n):
        arr.sort()
        head = 0
        tail = n-1
        new_arr = [0]*n
        i = 0
        while head <= tail:
            if i%2 != 0:
                new_arr[i] = arr[head]
                head += 1
                i += 1
                continue
            new_arr[i] = arr[tail]
            tail -= 1
            i += 1
        for i in range(n):
            arr[i] = new_arr[i]

Solution().rearrange([10,20,30,40,50,60,70,80,90,100,110],11)