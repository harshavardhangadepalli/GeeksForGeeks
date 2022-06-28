class Solution:
    def multiplyStrings(self,s1,s2):
        def summer(l):
            s = 0
            for item in l:
                s+=int(item)
            return s
        if len(s1) > len(s2):
            p2 = s2
            p1 = s1
        else:
            p2 = s1
            p1 = s2
        p1 = p1[::-1]
        p2 = p2[::-1]
        l = list()
        for i in range(len(p2)):
            carry = 0
            num = ''
            for j in range(len(p1)):
                temp = str((ord(p2[i])-48)*(ord(p1[j])-48)+carry)
                num += temp[-1]
                if len(temp[:len(temp)-1])==0:
                    carry = 0
                else:
                    carry = ord(temp[:len(temp)-1])-48
            if carry!=0:
                num += str(carry)
            num = num[::-1]
            l.append(num)
        for i in range(len(l)):
            l[i] = l[i]+'0'*i
        s = '0'
        return str((summer(l)))

Solution().multiplyStrings('6728','13')