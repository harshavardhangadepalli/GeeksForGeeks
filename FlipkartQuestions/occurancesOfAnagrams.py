class Solution:
    def search(self, pat, txt):
        # code here
        d1 = dict()
        d2 = dict()
        for _ in 'abcdefghijklmnopqrstuvwxyz':
            d1[_] = 0
            d2[_] = 0
        for _ in pat:
            d1[_]+=1
        if len(pat) > len(txt):
            return 0

        i = 0
        j = len(pat)-1
        count = 0
        for x in range(j+1):
            d2[txt[x]]+=1
        if d1 == d2:
            count+=1

        while j+1 < len(txt):
            d2[txt[i]]-=1
            i+=1
            j+=1
            d2[txt[j]]+=1
            if d1==d2:
                count+=1
        return count
        
Solution().search('aaba','aabaabaa')