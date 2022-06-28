import math
import heapq
class Solution:
    def networkDelayTime(self, times, n, k):
        adj = dict()
        for i in range(1,n+1):
            adj[i] = []
        for s,d,w in times:
            adj[s].append((d,w))
        distances = dict()
        for _ in range(1,n+1):
            distances[_] = float(math.inf)
        distances[k] = 0
        minheap = [(0,k)]
        while minheap:
            w,u = heapq.heappop(minheap)
            for v,weight in adj[u]:
                if distances[v] > distances[u] + weight:
                    distances[v] = distances[u] + weight
                    heapq.heappush(minheap,(weight,v))
        m = 0
        for _ in distances:
            if distances[_] == float(math.inf):
                return -1
            m = max(m,distances[_])
        return m
        
        
Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2)