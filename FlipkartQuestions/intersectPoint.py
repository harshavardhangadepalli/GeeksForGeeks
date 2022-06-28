#Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1,head2):
    s1 = set()
    a = head1
    while a:
        s1.add(a)
        a = a.next
    b = head2
    while b:
        if b in s1:
            return b
        b = b.next