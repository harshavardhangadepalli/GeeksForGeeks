class Solution:

    # Function to find minimum time required to rot all oranges.
    def orangesRotting(self, grid):
        # Code here
        def visitor(item):
            i = item[0]
            j = item[1]
            if i+1 < len(grid):
                if grid[i+1][j] == 1:
                    new_rotten.append([i+1, j])
                    grid[i+1][j] = 2
            if j+1 < len(grid[0]):
                if grid[i][j+1] == 1:
                    new_rotten.append([i, j+1])
                    grid[i][j+1] = 2
            if i-1 >= 0:
                if grid[i-1][j] == 1:
                    new_rotten.append([i-1, j])
                    grid[i-1][j] = 2
            if j-1 >= 0:
                if grid[i][j-1] == 1:
                    new_rotten.append([i, j-1])
                    grid[i][j-1] = 2

        new_rotten = list()
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 2:
                    new_rotten.append([i, j])
        if len(new_rotten) == 0:
            return -1
        count = 0
        while len(new_rotten) > 0:
            count += 1
            temp = new_rotten[::]
            new_rotten = list()
            for item in temp:
                visitor(item)
        for item in grid:
            for thing in item:
                if thing == 1:
                    return -1
        return count-1


print(Solution().orangesRotting(
    [
        [0, 1, 2],
        [0, 1, 2],
        [2, 1, 1]
    ]
))
