class Solution:
    # User function Template for python3
    # arr[]: Input Array
    # N : Size of the Array arr[]
    # Function to count inversions in the array.
    def __init__(self):
        self.count = 0

    def inversionCount(self, arr, n):
        # Your Code Here
        def merge_sort(l):
            if len(l) == 0:
                return list()
            if len(l) == 1:
                return l
            if len(l) == 2:
                left = [l[0]]
                right = [l[1]]
                final = merge(left, right)
            else:
                mid = len(l)//2
                left = merge_sort(l[0:mid])
                right = merge_sort(l[mid:])
                final = merge(left, right)
            return final

        def merge(arr1, arr2):
            if len(arr1) == 0 and len(arr2) == 0:
                return list()
            if len(arr1) == 0:
                return arr2
            if len(arr2) == 0:
                return arr1
            final = list()
            i = 0
            j = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] > arr2[j]:
                    self.count += len(arr1)-i
                    final.append(arr2[j])
                    j += 1
                else:
                    final.append(arr1[i])
                    i += 1
            if i < len(arr1):
                for x in range(i, len(arr1)):
                    final.append(arr1[x])
            if j < len(arr2):
                for x in range(j, len(arr2)):
                    final.append(arr2[x])
            return final
        merge_sort(arr)
        return self.count


print(Solution().inversionCount([3,1,2], 4))
