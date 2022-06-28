class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        prev = None
        current = head
        n = None
        while current:
            n = current.next
            current.next = prev
            prev = current
            current = n
        return prev