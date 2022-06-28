class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        curr_leader = A[N-1]
        leaders = list()
        for i in range(N):
            if A[N-i-1] >= curr_leader:
                leaders.append(A[N-i-1])
                curr_leader = A[N-i-1]
        return leaders[::-1]