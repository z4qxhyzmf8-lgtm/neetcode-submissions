class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid) #nr of rows
        m = len(grid[0]) #nr of cols
        def clear(i, j):
            nonlocal n
            nonlocal m

            if i < 0 or j < 0 or i >= n or j >= m:
                return
            if grid[i][j] == '0':
                return

            grid[i][j] = '0'

            clear(i + 1, j)
            clear(i - 1, j)
            clear(i, j + 1)
            clear(i, j - 1)

            return
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    clear(i, j)
        return count


        