    def isAnagram(self,a,b):
        #code here
        d1 = dict()
        d2 = dict()
        for _ in 'abcdefghijklmnopqrstuvwxxyz':
            d1[_] = 0
            d2[_] = 0
        for item in a:
            d1[item] += 1
        for item in b:
            d2[item] += 1
        if d1 == d2:
            return True
        return False