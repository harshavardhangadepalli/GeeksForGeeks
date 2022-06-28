class Solution:

    #Function to find unit area of the largest region of 1s.
	def findMaxArea(self, grid):
		def recursion(i,j,count):
			#visit all eight directions
			if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
				return count
			if visited[i,j] == True:
				return count
			if grid[i][j] == 0:
				return count
			# now we call all directions
			if grid[i][j] == 1:
				visited[i,j] = True
				count+=1
				#now we check all directions
				count = recursion(i,j+1,count)
				count = recursion(i,j-1,count)
				count = recursion(i+1,j,count)
				count = recursion(i-1,j,count)
				count = recursion(i+1,j+1,count)
				count = recursion(i-1,j-1,count)
				count = recursion(i+1,j-1,count)
				count = recursion(i-1,j+1,count)
			return count
		visited = dict()
		max_count = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				visited[i,j] = False
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if visited[i,j]==False:
					max_count = max(recursion(i,j,0),max_count)
		return(max_count)

print(Solution().findMaxArea(
	[
		[1,0],
		[1,1]
	]
	))