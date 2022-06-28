def countLeaves(root):
    # Code here
    l = list()
    def traversal(root):
        if not root.left and not root.right:
            l.append(root)
            return
        if root.left:
            traversal(root.left)
        if root.right:
            traversal(root.right)
    traversal(root)
    return len(l)