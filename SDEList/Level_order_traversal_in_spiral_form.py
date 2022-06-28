def findSpiral(root):
    # Code here
    d = dict()
    i = 0
    if not root:
        return root
    d[0] = [root]
    while True:
        if i not in d:
            break
        for item in d[i]:
            if item.left or item.right:
                if i+1 not in d:
                    d[i+1] = []
                if item.left:
                    d[i+1].append(item.left)
                if item.right:
                    d[i+1].append(item.right)
        i+=1
    ret = []
    ret.append(root)
    i = 1
    while True:
        if i not in d:
            break
        if i % 2 != 0:
            ret += d[i]
        else:
            ret += d[i][::-1]
    return ret