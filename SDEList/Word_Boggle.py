class Solution:
    def wordBoggle(self,board,dictionary):
        # return list of words(str) found in the board
        def isvalid(word):
            if word in prefixes:
                return True
            return False

        def dfs(i,j,word):
            for valid in dictionary:
                if word == valid:
                    words_list.add(word)
            if not isvalid(word):
                return
            visited.add((i,j))
            l = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
            for item in l:
                i1 = i + item[0]
                j1 = j + item[1]
                if i1 < 0 or j1 < 0 or i1 >= len(board) or j1 >= len(board[0]):
                    continue
                if (i1,j1) in visited:
                    continue
                dfs(i1,j1,word+board[i1][j1])
            visited.remove((i,j))

        def construct_prefixes(word):
            for i in range(len(word)+1):
                prefixes.add(word[0:i])
            return
                
        # need to perform dfs on all elements
        words_list = set()
        d = dict()
        visited = set()
        prefixes = set()
        for item in dictionary:
            construct_prefixes(item)
        prefixes.remove('')
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                dfs(i,j,board[i][j])
        return list(words_list)

print(Solution().wordBoggle([['G','I','Z'],['U','E','K'],['Q','S','E']],["GEEKS","FOR","QUIZ","GO","UEK"]))