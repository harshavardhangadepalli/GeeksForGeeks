class Solution:
    #Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        # code here
        if not head:
            return None
        
        ptr = head
        count = 0
        old_list = list()
        indices = dict()
        while ptr:
            old_list.append(ptr)
            indices[ptr] = count
            count+=1
            ptr = ptr.next

        new_list = list()
        for i in range(len(old_list)):
            new_list.append(Node(data=old_list[i].data))

        for i in range(len(new_list)):
            if i+1 < len(new_list):
                new_list[i].next = new_list[i+1]
        # for i in range(len(old_list)):
        #     print(str(old_list[i].data)+"  "+str(new_list[i].data))

        for i in range(len(old_list)):
            if old_list[i].arb != None:
                new_list[i].arb = new_list[indices[old_list[i].arb]]
        return new_list[0]