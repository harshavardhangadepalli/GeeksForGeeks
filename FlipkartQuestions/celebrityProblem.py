class Solution:
    
    # Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        # the only ones that can be celebrities are the ones that have all zeroes
        # if the [i][i] element is zero only then it is a potential celebrity
        def knows(a,b):
            return M[a][b]
        i = 0
        j = n-1
        while i < j:
            if knows(j,i):
                j-=1
            else:
                i+=1
        # i is the potential celeb
        c = 0
        for j in range(n):
            if j==i:
                continue
            if M[i][j]==1 or M[j][i]!=1:
                return -1
        return i

print(Solution().celebrity(
    [
        [0,1],
        [1,0]
    ]
    ,2))