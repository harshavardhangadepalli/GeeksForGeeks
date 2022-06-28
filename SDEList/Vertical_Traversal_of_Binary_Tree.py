class Solution:
    
    #Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root): 
        #Your code here
        d = dict()
        level = 0
        if not root:
            return []
        d[0] = [root]
        while level in d:
            for item in d[level]:
                if item.left or item.right:
                    if level+1 not in d:
                        d[level+1] = []
                    if item.left:
                        d[level+1].append(item.left)
                    if item.right:
                        d[level+1].append(item.right)
            level += 1
        # d has the level order traversal
        
        # d1 has the horizontal distance
        d1 = dict()
        def solve(root,dist):
            if not root:
                return
            d1[root] = dist
            solve(root.left,dist-1)
            solve(root.right,dist+1)
        solve(root,0)
        
        
        d2 = dict()
        level = 0
        while level in d:
            for item in d[level]:
                index = d1[item]
                if index in d2:
                    d2[index].append(item.data)
                else:
                    d2[index] = [item.data]
            level += 1
        ret = []
        for key in sorted(d2.keys()):
            for item in d2[key]:
                ret.append(item)
        return ret