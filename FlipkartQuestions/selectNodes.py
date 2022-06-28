#User function Template for python3

class Solution:
    def __init__(self):    
        self.min_count = 0
        self.total = 0
    def countVertex(self, N, edges):
        #code here
        def recursion(current_set,remaining_set,current_edges_set):
            if tuple(current_set) in dp:
                return
            else:
                dp[tuple(current_set)] = True
            if len(current_edges_set) == self.total:
                self.min_count = min(self.min_count,len(current_set))
            if len(current_set) > self.min_count:
                return
            # if all the elements are not included, we need to include one of the remaining element
            for item in remaining_set:
                new_remaining = remaining_set.copy()
                new_remaining.remove(item)
                new_current = current_set.copy()
                new_current.add(item)
                new_edges = current_edges_set.copy()
                for thing in d[item]:
                    new_edges.add(tuple(thing))
                recursion(new_current,new_remaining,new_edges)

        # the minimum count is initally n
        self.min_count = N
        dp = dict()
        nodes_set = set()
        for i in range(1,N+1):
            nodes_set.add(i)
        edges_set = set()
        for item in edges:
            edges_set.add(tuple(item))
        d = dict()
        for i in range(1,N+1):
            for item in edges_set:
                if i in item:
                    if i not in d:
                        d[i] = list()
                    d[i].append(item)
        self.total = len(edges_set)
        recursion(set(),nodes_set,set())
        return(self.min_count)

Solution().countVertex(3,[[1,2],[1,3]])