class Solution:
    def floorSqrt(self, x):
        if x == 1:
            return 1
        if x == 2:
            return 1
        start = 1
        end = x
        while end - start > 1:
            mid = (start+end)//2
            #print(mid)
            if mid*mid == x:
                return mid
            else:
                if mid*mid < x:
                    start = mid
                else:
                    end = mid
        #print(end)
        #print(start)
        if start*start < x and end*end < x:
            return max(start,end)
        if start*start < x and end*end > x:
            return start
        return end

print(Solution().floorSqrt(90))