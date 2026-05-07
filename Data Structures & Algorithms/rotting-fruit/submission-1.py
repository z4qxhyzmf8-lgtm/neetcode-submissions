class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = set() 

        def check(i, j):
            nonlocal n, m

            if i < 0 or j < 0 or i >= n or j >= m or (i, j) in vis or grid[i][j] == 0:
                return False
            return True
        
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    vis.add((i, j))
        time = 0
        while q:
            k = len(q)
            for i in range(k):
                r, c, d = q.popleft()
                time = max(d , time)

                if check(r + 1, c):
                    q.append((r + 1, c, d + 1))
                    vis.add((r + 1, c))
                    grid[r + 1][c] = 2

                if check(r - 1, c):
                    q.append((r - 1, c, d + 1))
                    vis.add((r - 1, c))
                    grid[r - 1][c] = 2
                
                if check(r, c + 1):
                    q.append((r, c + 1, d + 1))
                    vis.add((r, c + 1))
                    grid[r][c + 1] = 2
                
                if check(r, c - 1):
                    q.append((r, c - 1, d + 1))
                    vis.add((r, c - 1))
                    grid[r][c - 1] = 2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return time
        
