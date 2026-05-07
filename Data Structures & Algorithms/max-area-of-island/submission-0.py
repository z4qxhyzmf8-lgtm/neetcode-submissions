class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid) #nr of rows
        m = len(grid[0]) #nr of cols
        max_area = 0
        def area(i, j):
            nonlocal n, m

            if i < 0 or j < 0 or i >= n or j >= m:
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            A = (area(i + 1, j) + 
                area(i - 1, j) +
                area(i, j + 1) +
                area(i, j - 1))
            return 1 + A
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_area = max(max_area, area(i, j))
        return max_area 


        