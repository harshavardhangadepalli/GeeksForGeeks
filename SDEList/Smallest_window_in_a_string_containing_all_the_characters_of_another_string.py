class Solution:
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    
    def smallestWindow(self, s, p):
        d = dict()
        for _ in 'abcdefghijklmnopqrstuvwxyz':
            d[_] = 0
        for item in p:
            d[item] += 1      
Solution().smallestWindow('zoomlazapzo','oza')