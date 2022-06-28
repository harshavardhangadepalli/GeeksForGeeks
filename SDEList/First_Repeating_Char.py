class Solution:

    def firstRepChar(self, s):
        # code here
        a = set()
        for item in s:
            if item in a:
                return item
            else:
                a.add(item)
        return -1