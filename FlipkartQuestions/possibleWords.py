class Solution:
    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self,a,N):
        #Your code here
        d = dict()
        d[2] = 'abc'
        d[3] = 'def'
        d[4] = 'ghi'
        d[5] = 'jkl'
        d[6] = 'mno'
        d[7] = 'pqrs'
        d[8] = 'tuv'
        d[9] = 'wxyz'

        l = list()
        for item in d[a[0]]:
            l.append(item)
        for i in range(1,N):
            new_list = list()
            for item in l:
                for new_item in d[a[i]]:
                    new_list.append(item+new_item)
            l = new_list[::]
        return(l)
print(Solution().possibleWords([2,3,4],3))