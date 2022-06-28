class DJS:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return False
        if self.rank[a] > self.rank[b]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]
        return True

    def find(self, a):
        if self.parent[a] == a:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]


class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):
        # Code here
        # each row in adj represents a vertex, and each item in row represents that edge between
        # vertex and item is present
        dsj = DJS(V)
        edges = set()
        for i in range(len(adj)):
            for j in adj[i]:
                if (i,j) in edges or (j,i) in edges:
                    continue
                # now for every edge, add it to the dsj
                if not dsj.union(i,j):
                    # this means cycle exists
                    return 1
                edges.add((i,j))
        return 0

print(Solution().isCycle(5,
    [
        [4],
        [2,4],
        [1,3],
        [2,4],
        [0,1,3]
    ]
    ))