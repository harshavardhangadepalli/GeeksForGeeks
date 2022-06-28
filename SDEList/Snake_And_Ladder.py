class Solution:
    def minThrow(self, N, arr):
        self.count = 0
        # code here
        def visitor(i):
            l = [1,2,3,4,5,6]
            for item in l:
                if i + item == 30:
                    return True
                if i + item > 30:
                    continue
                if i + item in snakes:
                    new_nodes.append(snakes[i+item])
                    continue
                if i + item in ladders:
                    new_nodes.append(ladders[i+item])
                    continue
                new_nodes.append(i+item)
        snakes = dict()
        ladders = dict()
        for i in range(0,2*N,2):
            if arr[i] < arr[i + 1]:
                ladders[arr[i]] = arr[i+1]
            else:
                snakes[arr[i]] = arr[i+1]
        new_nodes = list()
        new_nodes.append(1)
        flag = 0
        while len(new_nodes) > 0:
            self.count += 1
            l = new_nodes[::]
            new_nodes = list()
            for item in l:
                flag = visitor(item)
                if flag:
                    break
            if flag:
                break
        return self.count

Solution().minThrow(8, [3, 22, 5, 8, 11, 26, 20, 29, 17, 4, 19, 7, 27, 1, 21, 9])