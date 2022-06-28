
class Solution:
    def numIslands(self,grid):
        #code here
        def visitor(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            if (i,j) in visited:
                return
            if grid[i][j] == 0:
                return
            visited.add((i,j))
            if grid[i][j] == 1:
                # n, s, e, w, ne, nw, se, sw
                visitor(i,j+1)
                visitor(i,j-1)
                visitor(i+1,j)
                visitor(i-1,j)
                visitor(i-1,j+1)
                visitor(i+1,j+1)
                visitor(i-1,j-1)
                visitor(i+1,j-1)
        visited = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j]==1:
                    count+=1
                    visitor(i,j)
        return(count)

print(Solution().numIslands(
    [
        [0,1,1,1,0,0,0],
        [0,0,1,1,0,1,0]
    ]
    ))