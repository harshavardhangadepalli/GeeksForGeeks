class DJS:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    #union of two nodes, a and b
    #find of (a) will return parent of a
    def union(self,a,b):
        pa = self.find(a)
        pb = self.find(b)
        if pa==pb: return
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa]+=self.rank[pb]
        else:
            self.parent[pa] = pb
            self.rank[pb]+=self.rank[pa]

    def find(self,a):
        if self.parent[a] == a:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]



class Solution:
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #each row in adj corresponds to some index i
        #each row has two entries, which node i connects to, and weight of that node
        edges_list = dict()
        for i in range(V):
            for item in adj[i]:
                if item[1] in edges_list:
                    edges_list[item[1]].append([i,item[0]])
                else:
                    edges_list[item[1]] = list()
                    edges_list[item[1]].append([i,item[0]])
        weight_list = sorted(edges_list.keys())
        ds = DJS(V)
        count = 0
        flag = 0
        summer = 0
        for weight in weight_list:
            if flag == 1:
                break
            for edge in edges_list[weight]:
                if count == V-1:
                    flag = 1
                    break
                if ds.find(edge[0]) != ds.find(edge[1]):
                    ds.union(edge[0],edge[1])
                    summer+=weight
        print(summer)