#User function Template for python3
found = 0
def wordBreak(line, dictionary):
    hash_set = set()
    # Complete this function
    global found
    found = 0
    def recursion(s):
        global found
        if found == 1:
            return
        if s in hash_set:
            return
        if len(s) == 0:
            found = 1
            return
        hash_set.add(s)
        for item in dictionary:
            size = len(item)
            if size > len(s):
                continue
            if item == s[:size]:
                recursion(s[size:])
    if line == "":
        return found
    recursion(line)
    return found

wordBreak("",['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango'])