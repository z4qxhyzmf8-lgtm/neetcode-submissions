class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        def check(i, j, h, vis):
            nonlocal n, m
            if i < 0 or j < 0 or i >= n or j >= m or (i, j) in vis:
                return False
            if h > heights[i][j]:
                return False
            return True

        def bfs(sources, grid):
            nonlocal n, m
            vis = set()
            for i, j in sources:
                vis.add((i, j))
                grid[i][j] = True
            while sources:
                k = len(sources)
                for c in range(k):
                    i, j = sources.popleft()
                 
                    if check(i + 1, j, heights[i][j], vis):
                        sources.append([i + 1, j])
                        vis.add((i + 1, j))
                        grid[i + 1][j] = True

                    if check(i - 1, j, heights[i][j], vis):
                        sources.append([i - 1, j])
                        vis.add((i - 1, j))
                        grid[i - 1][j] = True
                    
                    if check(i, j + 1, heights[i][j], vis):
                        sources.append([i, j + 1])
                        vis.add((i, j + 1))
                        grid[i][j + 1] = True

                    if check(i, j - 1, heights[i][j], vis):
                        sources.append([i, j - 1])
                        vis.add((i, j - 1))
                        grid[i][j - 1] = True
        sol = []
        pacific = [[False for _ in range(m)] for _ in range(n)]
        atlantic = [[False for _ in range(m)] for _ in range(n)]
        p_sources = deque()
        a_sources = deque()
        for i in range(n):
            p_sources.append((i, 0))
            a_sources.append((i, m - 1))
        for j in range(1, m):
            p_sources.append((0, j))
            a_sources.append((n - 1, j - 1))
        bfs(p_sources, pacific)
        bfs(a_sources, atlantic)
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    sol.append([i, j])
        return sol

        