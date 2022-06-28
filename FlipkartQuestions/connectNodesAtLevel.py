#User function Template for python3
class Solution:
    #Function to connect nodes at same level.
    def connect(self, root):
        d = dict()
        i = 0
        d[i] = [root]
        while True:
            if i in d:
                for item in d[i]:
                    if item.left or item.right:
                        if i+1 in d:
                            if item.left:
                                d[i+1].append(item.left)
                            if item.right:
                                d[i+1].append(item.right)
                        else:
                            d[i+1] = list()
                            if item.left:
                                d[i+1].append(item.left)
                            if item.right:
                                d[i+1].append(item.right)

            else:
                break
            i+=1
        for i in range(1,len(d)):
            for j in range(len(d[i])):
                if j+1 < len(d[i]):
                    d[i][j].nextRight = d[i][j+1]
        return d[0]