class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        parents = [0]*V
        for i in range(V):
            parents[i] = i
        #print(parents)
        for edges in adj:
            print(edges)