class Solution:
    def isCircle(self, N, A):
        d = dict()
        visited = dict()
        for _ in 'abcdefghijklmnopqrstuvwxyz':
            d[_] = list()
        for i in range(1,N):
            word = A[i]
            d[word[0]].append(word)
            visited[word] = False
        visited[A[0]] = True
        first_letter = A[0][0]
        current_letter = A[0][-1]
        flag = False
        count = 1
        words_list = list()
        words_list.append(A[0])
        while True:
            if len(words_list) == N:
                flag = False
                break
            # if there are no words left with the starting letter(previous ending letter)
            if len(d[current_letter]) == 0:
                flag = True
                break
            new_word = d[current_letter][0]
            d[current_letter] = d[current_letter][1:]
            visited[new_word] = True
            current_letter = new_word[-1]
            words_list.append(new_word)
        if flag == True:
            return 0
        if words_list[-1][-1] == first_letter:
            return 1
        return 0

print(Solution().isCircle(3, ['cdc','cgc','csc']))
