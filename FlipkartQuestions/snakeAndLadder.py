class Solution:
    def minThrow(self, N, arr):
        # code here
        # we need to bfs, and the first time that the solution is reached will be the number of tosses
        snakes = dict()
        ladders = dict()

        # creating snakes and ladders:
        i = 0
        while True:
            if i+1 >= len(arr):
                break
            if arr[i] > arr[i+1]:
                # this means it is a snake
                snakes[arr[i]] = arr[i+1]
                i += 2
            else:
                ladders[arr[i]] = arr[i+1]
                i += 2

        bfs = dict()
        current_level = 0
        ans = -1
        bfs[current_level] = list()
        if 1 in ladders:
            bfs[current_level].append(ladders[1])
        else:
            bfs[current_level].append(1)


        while current_level in bfs:
            if ans != -1:
                break
            for item in bfs[current_level]:
                if ans != -1:
                    break
                if current_level+1 not in bfs:
                    bfs[current_level+1] = list()
                for i in range(1,7):
                    temp = item + i
                    if temp == 30:
                        ans = current_level + 1
                        break
                    if temp > 30:
                        continue
                    if temp in ladders:
                        temp = ladders[temp]
                    elif temp in snakes:
                        temp = snakes[temp]
                    bfs[current_level+1].append(temp)
            current_level += 1
        return ans
                    



print(Solution().minThrow(8,
    [3, 22, 5, 8, 11, 26, 20, 29, 
       17, 4, 19, 7, 27, 1, 21, 9]
    ))