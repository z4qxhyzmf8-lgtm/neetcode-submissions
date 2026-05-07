class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        row_0, col_0 = False, False

        for i in range(n):
            for j in range(m):
                if not matrix[i][j]:
                    if j:
                        matrix[0][j] = '*'
                    else:
                        col_0 = True

                    if i:
                        matrix[i][0] = '*'
                    else:
                        row_0 = True

        for i in range(n):
            if matrix[i][0] == '*':
                for j in range(m):
                    matrix[i][j] = 0
        
        for j in range(m):
            if matrix[0][j] == '*':
                for i in range(n):
                    matrix[i][j] = 0

        if row_0:
            for j in range(m):
                matrix[0][j] = 0
        if col_0:
            for i in range(n):
                matrix[i][0] = 0            

        
         
        
        