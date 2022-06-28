def sortedMerge(head1, head2):
    dummy = Node(data=0)
    ptr = dummy
    ptr1 = head1
    ptr2 = head2
    while ptr1 and ptr2:
        if ptr1.data <= ptr2.data:
            ptr.next = ptr1
            ptr1 = ptr1.next
            ptr = ptr.next
        else:
            ptr.next = ptr2
            ptr2 = ptr2.next
            ptr = ptr.next
    while ptr1:
        ptr.next = ptr1
        ptr1 = ptr1.next
        ptr = ptr.next
    while ptr2:
        ptr.next = ptr2
        ptr2 = ptr2.next
        ptr = ptr.next
    return dummy.next