import heapq
import math
class Solution:
    def minimumEffortPath(self, heights):
        m,n = len(heights),len(heights[0])
        distance = [[math.inf] * n for _ in range(m)]
        distance[0][0] = 0
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        adj = dict()
        for i in range(m):
            for j in range(n):
                adj[(i,j)] = list()
                for x,y in directions:
                    i1,j1 = i + x, j + y
                if 0 <= i1 < m and 0 <= j1 < n:
                    weight = abs(heights[i][j] - heights[i1][j1])
                    adj[(i,j)].append(((i1,j1),weight))
        minheap = [(0,0,0)]
        for i in 
        while minheap:
            d,r,c = heapq.heappop(minheap)
            for x,y in l:
                r1 = r + x
                c1 = c + y
                if 0 <= r1 < m and 0 <= c1 < n:
                    weight = max(d,abs(heights[r1][c1]-heights[r][c]))
                    if distance[r1][c1] > weight:
                        distance[r1][c1] = weight
                        heapq.heappush(minheap,(distance[r1][c1],r1,c1))
        return distance[m-1][n-1]