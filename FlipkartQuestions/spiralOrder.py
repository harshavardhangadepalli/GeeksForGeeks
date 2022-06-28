class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix, r, c):
        visited = dict()
        for i in range(r):
            for j in range(c):
                visited[(i, j)] = False
        visited[(0,0)] = True
        v_count = 1
        current_dir = 'right'
        i = 0
        j = 0
        l = list()
        l.append(matrix[0][0])

        def can_visit(i,j,direction):
            if direction=='right':
                if j+1 >= c:
                    return False
                if visited[(i,j+1)]==True:
                    return False
                return True
            if direction == 'down':
                if i+1 >= r:
                    return False
                if visited[(i+1,j)] == True:
                    return False
                return True
            if direction == 'left':
                if j-1 < 0:
                    return False
                if visited[(i,j-1)] == True:
                    return False
                return True
            if direction == 'up':
                if i-1 < 0:
                    return False
                if visited[(i-1,j)] == True:
                    return False
                return True

        def visit(i,j,direction):
            if direction=='right':
                visited[(i,j+1)] = True
                l.append(matrix[i][j+1])
                return i,j+1
            if direction == 'down':
                visited[(i+1,j)] = True
                l.append(matrix[i+1][j])
                return i+1,j
            if direction == 'left':
                visited[(i,j-1)] = True
                l.append(matrix[i][j-1])
                return i,j-1
            if direction == 'up':
                visited[(i-1,j)] = True
                l.append(matrix[i-1][j])
                return i-1,j

        while True:
            if v_count == r*c:
                break
            if current_dir == 'right':
                while can_visit(i, j, 'right'):
                    #print(i,j)
                    i,j = visit(i, j, 'right')
                    v_count+=1
                current_dir = 'down'
            if current_dir == 'down':
                while can_visit(i, j, 'down'):
                    i, j = visit(i, j, 'down')
                    #print(i,j)
                    v_count+=1
                current_dir = 'left'
            if current_dir == 'left':
                while can_visit(i,j,'left'):
                    #print(i,j)
                    i,j = visit(i,j,'left')
                    v_count+=1
                current_dir = 'up'
            if current_dir == 'up':
                #print(i,j)
                while can_visit(i,j,'up'):
                    i,j = visit(i,j,'up')
                    v_count+=1
                current_dir = 'right'
        #print(l)
        return l

print(Solution().spirallyTraverse(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4, 4))
