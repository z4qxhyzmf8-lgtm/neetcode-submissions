class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if not matrix[i][j]:
                    self.mark(i, j, n, m, matrix)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '*':
                    matrix[i][j] = 0
    def mark(self, i, j, n, m, matrix):
        for x in range(n):
            if matrix[x][j]:
                matrix[x][j] = '*'
        for y in range(m):
            if matrix[i][y]:
                matrix[i][y] = '*' 
        
        