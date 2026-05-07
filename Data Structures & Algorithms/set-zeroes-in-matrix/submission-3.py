class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        row_0, col_0 = False, False

    
        for j in range(m):
            if not matrix[0][j]:
                row_0 = True
        for i in range(n):
            if not matrix[i][0]:
                col_0 = True

        for i in range(1, n):
            for j in range(1, m):
                if not matrix[i][j]:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        
        for i in range(1, n):
            for j in range(1, m):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if row_0:
            for j in range(m):
                matrix[0][j] = 0
        if col_0:
            for i in range(n):
                matrix[i][0] = 0