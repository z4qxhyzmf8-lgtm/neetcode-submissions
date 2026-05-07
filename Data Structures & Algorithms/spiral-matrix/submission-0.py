class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        
        n = len(matrix)
        m = len(matrix[0])

        elems = n * m
        count = 0
        i, j = 0, 0
        while count < elems:
            count += self.border(ans, i, j, n, m, matrix)
            i += 1
            j += 1
            n -= 1
            m -= 1
        return ans
    def border (self, ans, i, j, n, m, matrix):
        count = 0
        for y in range(j, m):
            count += 1
            ans.append(matrix[i][y])
        for x in range(i + 1, n):
            count += 1
            ans.append(matrix[x][m - 1])
        if n - 1 > i:
            for y in range(m - 2, j - 1, -1):
                count += 1
                ans.append(matrix[n - 1][y])
        if m - 1 > j:
            for x in range(n - 2, i, -1):
                count += 1
                ans.append(matrix[x][j])
        return count
        