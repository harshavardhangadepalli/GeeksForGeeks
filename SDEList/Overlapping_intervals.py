class Solution:
    def overlappedInterval(self, intervals):
        #Code here
        intervals.sort()
        new_list = list()
        new_list.append([intervals[0][0],intervals[0][1]])
        for i in range(1,len(intervals)):
            if new_list[-1][1] >= intervals[i][0]:
                new_list[-1][1] = max(intervals[i][1],new_list[-1][1])
            else:
                new_list.append([intervals[i][0],intervals[i][1]])
        return new_list
            
        
        
Solution().overlappedInterval([[1,3], [2,4], [6,8], [7,10]])