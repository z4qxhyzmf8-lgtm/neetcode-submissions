class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid) #nr of rows
        m = len(grid[0]) #nr of cols

        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append([i, j, 0])
        vis = {}
        while q:
            k = len(q)
            for i in range(k):
                r, c, d = q.popleft()
                vis[(r, c)] = 1
                if r - 1 >= 0 and (r - 1, c) not in vis:
                    grid[r - 1][c] = min(grid[r - 1][c], d + 1)
                    if grid[r - 1][c] > -1:
                        q.append((r - 1, c, d + 1))
                        
                if c - 1 >= 0 and (r, c - 1) not in vis:
                    grid[r][c - 1] = min(grid[r][c - 1], d + 1)
                    if grid[r][c - 1] > -1:
                        q.append((r, c - 1, d + 1))

                if r + 1 < n and (r + 1, c) not in vis:
                    grid[r + 1][c] = min(grid[r + 1][c], d + 1)
                    if grid[r + 1][c] > -1:
                        q.append((r + 1, c, d + 1))

                if c + 1 < m and (r, c + 1) not in vis:
                    grid[r][c + 1] = min(grid[r][c + 1], d + 1)
                    if grid[r][c + 1] > -1:
                        q.append((r, c + 1, d + 1))
                
                