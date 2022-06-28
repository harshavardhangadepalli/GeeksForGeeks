def isSubset( a1, a2, n, m):
    s1 = set(a1)
    s2 = set(a2)
    for item in s2:
        if item not in s1:
            return 'No'
    return 'Yes'