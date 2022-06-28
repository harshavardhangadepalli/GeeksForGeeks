class Solution:
    def helpaterp(self, hospital):
        # code here
        def visitor(item):
            i = item[0]
            j = item[1]
            if j-1 >= 0:
                if hospital[i][j-1] == 1:
                    hospital[i][j-1] = 2
                    unvisited.append([i,j-1])
            if j+1 < len(hospital[0]):
                if hospital[i][j+1] == 1:
                    hospital[i][j+1] = 2
                    unvisited.append([i,j+1])
            if i-1 >= 0:
                if hospital[i-1][j] == 1:
                    hospital[i-1][j] = 2
                    unvisited.append([i-1,j])
            if i+1 < len(hospital):
                if hospital[i+1][j] == 1:
                    hospital[i+1][j] = 2
                    unvisited.append([i+1,j])
        # in each iteration, visit all neighboring nodes to current 2s
        # find all current 2s:
        count = 0
        unvisited = list()
        for i in range(len(hospital)):
            for j in range(len(hospital[0])):
                if hospital[i][j] == 2:
                    unvisited.append([i,j])
        #print(unvisited)
        if(len(unvisited)) == 0:
            print(-1)
            return -1

        while len(unvisited) > 0:
            count+=1
            l = unvisited[::]
            unvisited = list()
            for item in l:
                visitor(item)
        for item in hospital:
            for thing in item:
                if thing == 1:
                    return -1
        return count-1

print(Solution().helpaterp([
[2,1,0,2,1],
[1,0,1,2,1],
[1,0,0,2,1]
]
))