class Solution:
    def reverseWords(self, s):
        # code here
        old_list = s.split(".")
        new_list = list()
        for item in old_list:
            new_list.append(item[::-1])
        s_new = ''
        for item in new_list:
            s_new += item+'.'
        return s_new[:len(s_new)-1]


print(Solution().reverseWords("i.like.this.program.very.much"))
