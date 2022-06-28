class Solution:
    def orangesRotting(self,grid):
        self.count = 0
        self.grid = grid
        # 0 is an empty cell
        # 1 is fresh orange
        # 2 is rotten orange
        def rot_adjacent(i,j):
            l = [[-1,0],[1,0],[0,-1],[0,1]]
            for item in l:
                i1 = i+item[0]
                j1 = j+item[1]
                if i1 >= len(self.grid) or i1 < 0 or j1 >= len(self.grid[0]) or j1 < 0:
                    continue
                if self.grid[i1][j1] == 0:
                    continue
                if self.grid[i1][j1] == 1:
                    self.grid[i1][j1] = 2
                    new_rotten_oranges.append([i1,j1])
                
        new_rotten_oranges = list()
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 2:
                    new_rotten_oranges.append([i,j])
        
        while len(new_rotten_oranges) > 0:
            self.count += 1
            l = new_rotten_oranges[::]
            new_rotten_oranges = list()
            for orange in l:
                rot_adjacent(orange[0],orange[1])
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    return -1
        return self.count-1

print(Solution().orangesRotting([[2,2,0,1]]))