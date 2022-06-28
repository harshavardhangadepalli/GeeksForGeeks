
class Solution:
    def maximumPath(self, N, Matrix):
        def recursion(i, j):
            if j < 0 or j >= N:
                return -1
            if (i,j) in dp:
                return dp[(i,j)]
            if i == N-1:
                return Matrix[i][j]
            dp[(i,j)] = Matrix[i][j]+max(recursion(i+1, j),recursion(i+1, j-1),recursion(i+1, j+1))
            return dp[(i,j)]
        dp = dict()
        curr_max = -1
        for i in range(N):
            curr_max = max(recursion(0,i),curr_max)
        return(curr_max)

Solution().maximumPath(2,
    [
        [348,391],
        [618,193]
    ]
    )