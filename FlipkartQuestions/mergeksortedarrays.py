class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # code here
        # return merged list
        def merge(l1,l2):
            ptr1 = 0
            ptr2 = 0
            l_new = list()
            while ptr1 < len(l1) and ptr2 < len(l2):
                if l1[ptr1] <= l2[ptr2]:
                    l_new.append(l1[ptr1])
                    ptr1+=1
                else:
                    l_new.append(l2[ptr2])
                    ptr2+=1
            if ptr1 >= len(l1) and ptr2 < len(l2):
                l_new += l2[ptr2:]
            elif ptr1 < len(l1) and ptr2 >= len(l2):
                l_new += l1[ptr1:]
            return l_new
        
        new_list = arr[:]
        while(len(new_list)>1):
            arr = new_list[:]
            new_list = list()
            for i in range(0,len(arr),2):
                if i+1 < len(arr):
                    temp = merge(arr[i],arr[i+1])
                    new_list.append(temp)
                else:
                    new_list.append(arr[i])
        return new_list[0]
        


print(Solution().mergeKArrays([[1,2,3],[5,6,8],[4,5,9]],3))