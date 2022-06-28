def maxArea(A,le):
    #code here
    max_area = 0
    i = 0
    j = le - 1
    while i < j:
        temp = (j-i)*min(A[i],A[j])
        max_area = max(temp,max_area)
        if A[i] <= A[j]:
            i+=1
        else:
            j-=1
    return(max_area)

print(maxArea([3,1,2,4,5],5))