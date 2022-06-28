def getNthFromLast(head,n):
    #code here
    temp = head # used temp variable
    length = 0
    while temp:
        temp = temp.next
        length += 1
    if n > length:
        return -1
    temp = head
    for i in range(0, length - n):
        temp = temp.next
    return temp.data