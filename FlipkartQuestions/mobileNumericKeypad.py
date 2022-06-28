# User function Template for python3
class Solution:
    def getCount(self, N):
        # code here
        # dp will have the number of possible numbers starting with i and having length x as dp(i,x)
        dp = dict()
        neighbours = dict()
        for i in range(10):
            dp[(i,1)] = 1
        neighbours[0] = [0,8]
        neighbours[1] = [1,2,4]
        neighbours[2] = [1,2,3,5]
        neighbours[3] = [2,3,6]
        neighbours[4] = [1,4,5,7]
        neighbours[5] = [2,4,5,6,8]
        neighbours[6] = [3,5,6,9]
        neighbours[7] = [4,7,8]
        neighbours[8] = [0,5,7,8,9]
        neighbours[9] = [6,8,9]
        def recursion(start,length):
            if (start,length) in dp:
                return dp[(start,length)]
            temp = 0
            for neighbour in neighbours[start]:
                temp += recursion(neighbour,length-1)
            dp[(start,length)] = temp
            return dp[(start,length)]
        total = 0
        for i in range(10):
            total += recursion(i,N)
        return total
Solution().getCount(7)
