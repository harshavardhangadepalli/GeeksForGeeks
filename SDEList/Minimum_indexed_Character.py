class Solution:
    
    #Function to find the minimum indexed character.
    def minIndexChar(self,Str, pat): 
        #code here
        s1 = set(pat)
        s2 = set(Str)
        s3 = set()
        for item in s1:
            if item in s2:
                s3.add(item)
        for i in range(len(Str)):
            if Str[i] in s3:
                return i
        return -1