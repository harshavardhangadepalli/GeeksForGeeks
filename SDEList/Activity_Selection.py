class Solution:
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        # code here
        def solve(i,time):
            if i == n:
                return 0
            
        activities = list()
        for i in range(n):
            activities.append((start[i],end[i]))
        activities.sort()
        print(activities)

Solution().activitySelection(4,[1,3,2,5],[2,4,3,6])