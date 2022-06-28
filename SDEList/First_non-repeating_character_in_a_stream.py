class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None
        self.prev = None
class Deque:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
    def append(self,val):
        n = Node(val)
        self.head.next.prev = n
        n.next = self.head.next
        n.prev = self.head
        self.head.next = n
    def remove(self):
        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail
        return node.val
    def isEmpty(self):
        if self.head.next == self.tail:
            return True
        return False
    def get(self):
        node = self.tail.prev
        return node.val
class Solution:
    def FirstNonRepeating(self, A):
        d = dict()
        for _ in 'abcdefghijklmnopqrstuvwxyz':
            d[_] = 0
        dq = Deque()
        ans = ''
        for item in A:
            d[item] += 1
            if d[item] == 1:
                dq.append(item)
            if dq.isEmpty():
                ans += '#'
                continue
            if not dq.isEmpty():
                flag = False
                while not dq.isEmpty():
                    if d[dq.get()] == 1:
                        ans += dq.get()
                        flag = True
                        break
                    dq.remove()
            if flag == False:
                ans += '#'
        return ans
Solution().FirstNonRepeating('aabbdedeccczysdzys')