class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the Aay.
    def equilibriumPoint(self,A, N):
        # Your code here
        left_sum = []
        right_sum = []
    
        # Iterate from 0 to len(A)
        for i in range(len(A)):
    
            # If i is not 0
            if(i != 0):
                left_sum.append(left_sum[i-1]+A[i])
                right_sum.append(right_sum[i-1]+A[len(A)-1-i])
            else:
                left_sum.append(A[i])
                right_sum.append(A[len(A)-1])
    
        # Iterate from 0 to len(A)    
        for i in range(len(A)):
            if(left_sum[i] == right_sum[len(A) - 1 - i ]):
                return(i+1)
        return -1