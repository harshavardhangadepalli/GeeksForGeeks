class Solution:
    
    #Function to find whether a path exists from the source to destination.
    def is_Possible(self, grid):
        def visit(i,j):
            l = [[1,0],[-1,0],[0,1],[0,-1]]
            for item in l:
                i1 = i + item[0]
                j1 = j + item[1]
                if i1 >= len(grid) or i1 <0 or j1 >= len(grid[0]) or j1 < 0:
                    continue
                if (i1,j1) in visited:
                    continue
                visited[(i1,j1)] = True
                if grid[i1][j1] == 0:
                    continue
                if grid[i1][j1] == 2:
                    return True
                if grid[i1][j1] == 3:
                    new_nodes.append((i1,j1))
            return False
                
                
        visited = dict()
        # we need to do bfs from the source, and terminte each element that has a wall, or has already been visited.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    source = (i,j)
        new_nodes = list()
        new_nodes = [source]
        visited[source] = True
        flag = False
        while len(new_nodes) > 0:
            if flag == True:
                break
            l = new_nodes[::]
            new_nodes = list()
            for item in l:
                flag = visit(item[0],item[1])
                if flag:
                    break
        if flag:
            return 1
        return 0
print(Solution().is_Possible([[3,2,3,3,3,3,0],[0,0,0,3,3,3,3],[0,0,3,0,1,3,0],[3,3,0,0,0,3,3],[0,3,3,3,3,3,3],[3,0,3,3,0,0,3],[3,3,0,3,0,3,3]]))