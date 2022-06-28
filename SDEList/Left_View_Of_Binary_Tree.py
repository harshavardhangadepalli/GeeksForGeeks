def LeftView(root):
    # code here
    d = dict()
    i = 0
    if not root:
        return []
    d[0] = [root]
    while i in d:
        for item in d[i]:
            if item.left or item.right:
                if i+1 not in d:
                    d[i+1] = list()
                if item.left:
                    d[i+1].append(item.left)
                if item.right:
                    d[i+1].append(item.right)
        i += 1
    ans = list()
    i = 0
    while i in d:
        ans.append(d[i][0].data)
        i += 1
    return ans