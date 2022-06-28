class MinHeap:
    def __init__(self):
        self.a = [None]
    def insert(self,val):
        self.a.append(val)
        i = len(self.a) - 1
        if len(self.a) > 2:
            while self.a[i] < self.a[(int)(i/2)]:
                self.swap(i,(int)(i/2))
                i = (int)(i/2)
                if i <= 1:
                    break
    def extractmin(self):
        if len(self.a) <= 1:
            return None
        if len(self.a) == 2:
            return self.a.pop()
        min_element = self.a[1]
        last_element = self.a.pop()
        self.a[1] = last_element
        if len(self.a) == 3:
            if self.a[1] > self.a[2]:
                self.swap(1,2)
            return min_element
        else:
            # visit the two children of the index, and check if they are greater, move to appropriate side
            i = 1
            while True:
                left = i*2
                right = i*2 + 1
                if left >= len(self.a) or right >= len(self.a) or i >= len(self.a):
                    break
                # if the element is less than both children, return
                if self.a[i] < self.a[right] and self.a[i] < self.a[left]:
                    break
                if self.a[i] > self.a[right] and self.a[i] > self.a[left]:
                    if self.a[left] < self.a[right]:
                        # we will swap i with lesser element
                        self.swap(left,i)
                        i = left
                    else:
                        self.swap(right,i)
                        i = right
                # if it greater than one, move swap that and child, move i,left,right
                elif self.a[i] > self.a[right]:
                    self.swap(i,right)
                    i = right
                else:
                    self.swap(i,left)
                    i = left
            if left < len(self.a):
                if self.a[i] > self.a[left]:
                    self.swap(i,left)
            return min_element
    def swap(self,i1,i2):
        self.a[i1],self.a[i2] = self.a[i2],self.a[i1]
    def printer(self):
        print(self.a)

class MaxHeap:
    def __init__(self):
        self.heap = [None]
    def insert(self,val):
        self.heap.append(val)
        i = len(self.heap) - 1
        if len(self.heap) > 2:
            while self.heap[i] > self.heap[(int)(i/2)]:
                self.heap[i], self.heap[(int)(i/2)] = self.heap[(int)(i/2)], self.heap[i]
                i = (int)(i/2)
                if i<=1:
                    break
    def delete(self):
        if len(self.heap) <= 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        max_element = self.heap[1]
        last_element = self.heap.pop()
        self.heap[1] = last_element
        if len(self.heap) == 3:
            if self.heap[1] < self.heap[2]:
                self.heap[1],self.heap[2] = self.heap[2], self.heap[1]
                return max_element
        else:
            i = 1
            while True:
                left = i*2
                right = i*2 + 1
                if left >= len(self.heap) or right >= len(self.heap) or i >= len(self.heap):
                    break
                # if the current element is greater than both children
                if self.heap[i] > self.heap[left] and self.heap[i] > self.heap[right]:
                    break
                # if it is not greater than both
                if self.heap[i] < self.heap[left] and self.heap[i] < self.heap[right]:
                    if self.heap[left] > self.heap[right]:
                        self.heap[i],self.heap[left] = self.heap[left],self.heap[i]
                        i = left
                    else:
                        self.heap[i],self.heap[right] = self.heap[right],self.heap[i]
                        i = right
                    # if it is not lesser than both
                elif self.heap[i] < self.heap[left]:
                    self.heap[i],self.heap[left] = self.heap[left],self.heap[i]
                    i = left
                else:
                    self.heap[i],self.heap[right] = self.heap[right],self.heap[i]
                    i = right
            if left < len(self.heap):
                if self.heap[i] < self.heap[left]:
                    self.heap[i],self.heap[left] = self.heap[left],self.heap[i]
                    i = left
        return max_element
    def printer(self):
        print(self.heap)
a = MinHeap()
a.insert(20)
a.insert(17)
a.insert(21)
a.insert(25)
a.insert(40)
a.insert(42)
a.printer()
a.extractmin()
a.printer()