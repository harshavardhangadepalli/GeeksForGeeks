#User function Template for python3
class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        #code here
        self.count = 0
        def visit(i,j):
            l = [[1,0],[-1,0],[0,1],[0,-1]]
            for item in l:
                i1 = i + item[0]
                j1 = j + item[1]
                if i1 < 0 or j1 < 0 or i1 >= N or j1 >= M:
                    continue
                if (i1,j1) in visited:
                    continue
                visited.add((i1,j1))
                if i1 == X and j1 == Y:
                    return True
                if A[i1][j1] == 0:
                    continue
                if A[i1][j1] == 1:
                    new_nodes.append((i1,j1))
            return False
        new_nodes = list()
        if A[0][0] == 0:
            return -1
        if A[X][Y] == 0:
            return -1
        new_nodes = [(0,0)]
        visited = set()
        flag = False
        while len(new_nodes) > 0:
            self.count += 1
            l = new_nodes[::]
            new_nodes = list()
            for position in l:
                flag = visit(position[0],position[1])
                if flag:
                    break
            if flag:
                break
        if flag:
            return self.count
        return -1

print(Solution().shortestDistance(8,7,[[0,0,1,1,0,0,1],[1,0,1,0,1,0,1],[1,1,1,1,1,0,1],[0,1,0,1,0,1,1],[1,0,0,1,0,1,0],[1,1,0,1,1,1,1],[1,1,1,0,0,1,0],[0,1,1,1,1,0,1]],0,2))