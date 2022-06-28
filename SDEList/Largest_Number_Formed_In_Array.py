class Solution:
    def printLargest(self,arr):
        def greaterthan(s1,s2):
            if s1+s2 > s2+s1:
                return 1
            return 0
        def merge(l1,l2):
            if not len(l1) and not len(l2):
                return list()
            i = 0
            j = 0
            l = list()
            while i < len(l1) and j < len(l2):
                if not greaterthan(l1[i],l2[j]):
                    l.append(l2[j])
                    j += 1
                    continue
                l.append(l1[i])
                i += 1
            if i < len(l1):
                l += l1[i:]
            if j < len(l2):
                l += l2[j:]
            return l
        
        def merge_sort(l):
            if len(l) == 0:
                return list()
            if len(l) == 1:
                return l
            mid = len(l) // 2
            return merge(merge_sort(l[0:mid]), merge_sort(l[mid:]))
        arr = list(map(str,arr))
        arr = merge_sort(arr)
        s = ''
        for i in range(len(arr)):
            s += arr[i]
        return s
print(Solution().printLargest([3, 30, 34, 5, 9]))