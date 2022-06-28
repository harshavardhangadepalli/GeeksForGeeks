class Solution:
	#Function to find out minimum steps Knight needs to reach target position.
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
		#Code here
		x2 = TargetPos[0]-1
		y2 = TargetPos[1]-1
		x1 = KnightPos[0]-1
		y1 = KnightPos[1]-1
		if (x1,y1) == (x2,y2):
			return 0
		# we need to reach x2,y2 from x1,y1
		d = dict()
		visited = set()
		def can_be_visited(x,y):
			l = list()
			if x+2 < N:
				if y+1 < N:
					if (x+2,y+1) not in visited:
						l.append((x+2,y+1))
				if y-1 >= 0:
					if (x+2,y-1) not in visited:
						l.append((x+2,y-1))
			if x-2 >= 0:
				if y+1 < N:
					if (x-2,y+1) not in visited:
						l.append((x-2,y+1))
				if y-1 >= 0:
					if (x-2,y-1) not in visited:
						l.append((x-2,y-1))
			if x+1 < N:
				if y+2 < N:
					if (x+1,y+2) not in visited:
						l.append((x+1,y+2))
				if y-2 >= 0:
					if (x+1,y-2) not in visited:
						l.append((x+1,y-2))
			if x-1 >= 0:
				if y+2 < N:
					if (x-1,y+2) not in visited:
						l.append((x-1,y+2))
				if y-2 >= 0:
					if (x-1,y-2) not in visited:
						l.append((x-1,y-2))
			return l
		# level 0
		d[0] = list()
		d[0].append((x1,y1))
		# current level
		level = 0
		count = -1
		flag = False
		while True:
			if flag == True:
				break
			if level not in d:
				break
			for item in d[level]:
				if item == (x2,y2):
					visited.add(item)
					flag = True
					count = level
					break
				visited.add(item)
				l = can_be_visited(item[0],item[1])
				if len(l) == 0:
					continue
				if level+1 not in d:
					d[level+1] = list()
				for x in l:
					visited.add(x)
					d[level+1].append(x)
			level+=1
			d[level-1] = list()
		return count

print(Solution().minStepToReachTarget((62,234),(169,100),393))