class Solution:
    def min_number_swaps(self,arr):
        self.count = 0
        new_arr = arr[::]
        new_arr.sort()
        # hash map will contain the correct value at index 'i'
        hashmap = dict()
        indexof = dict()
        for i in range(len(arr)):
            hashmap[i] = new_arr[i]
            indexof[arr[i]] = i
        for i in range(len(arr)):
            if hashmap[i] == arr[i]:
                continue
            # else, we need to get the element that is supposed to be at index i.
            # that element will be hashmap[i]
            # get the index of this element in old array, and swap.
            # the two elements that are exchanged ar arr[index1] and arr[index2]
            index1 = i
            index2 = indexof[hashmap[i]]
            arr = self.swap(index1, index2,arr)
            temp = indexof[arr[index1]]
            indexof[arr[index1]] = indexof[arr[index2]]
            indexof[arr[index2]] = temp
        print(self.count)
    def swap(self,index1,index2,arr):
        self.count += 1
        temp = arr[index1]
        arr[index1] = arr[index2]
        arr[index2] = temp
        return arr
        sort(key=lambda x: x[1])
Solution().min_number_swaps([2,6,1,0,9,28,4,99])