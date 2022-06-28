class Solution:
    def __init__(self):
        self.x = 0
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c):
        
        def can_visit(direction,i,j):
            if direction == 'right':
                if j + 1 < c:
                    if matrix[i][j+1] != -1:
                        return True
                    return False
                return False
            if direction == 'down':
                if i + 1 < r:
                    if matrix[i+1][j] != -1:
                        return True
                    return False
                return False
            if direction == 'left':
                if j - 1 >= 0:
                    if matrix[i][j-1] != -1:
                        return True
                    return False
                return False
            if direction == 'up':
                if i - 1 >= 0:
                    if matrix[i-1][j] != -1:
                        return True
                    return False
                return False
        
        def visit(direction,i,j):
            self.x += 1
            if direction == 'right':
                l.append(matrix[i][j+1])
                matrix[i][j+1] = -1
                return [i,j+1]
            if direction == 'down':
                l.append(matrix[i+1][j])
                matrix[i+1][j] = -1
                return [i+1,j]
            if direction == 'left':
                l.append(matrix[i][j-1])
                matrix[i][j-1] = -1
                return [i,j-1]
            if direction == 'up':
                l.append(matrix[i-1][j])
                matrix[i-1][j] = -1
                return [i-1,j]
        l = list()
        l.append(matrix[0][0])
        matrix[0][0] = -1
        direction = 'right'
        i = 0
        j = 0
        self.x += 1
        while self.x < r*c:
            while(can_visit(direction,i,j)):
                i,j = visit(direction, i,j)
            if direction == 'right':
                direction = 'down'
                continue
            if direction == 'down':
                direction = 'left'
                continue
            if direction == 'left':
                direction = 'up'
                continue
            if direction == 'up':
                direction = 'right'
                continue
        return(l)

Solution().spirallyTraverse([[1,2,3],[4,5,6],[7,8,9]],3,3)