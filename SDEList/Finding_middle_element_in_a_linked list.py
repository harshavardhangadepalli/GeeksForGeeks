class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
            