class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        def check(i, j):
            nonlocal n, m, vis
            if i < 0 or j < 0 or i >= n or j >= m or (i, j) in vis:
                return False
            if board[i][j] == 'X':
                return False
            return True

        q = deque()
        grid = [[0 for _ in range(m)] for _ in range(n)]
        vis = set()
        for i in range(n):
            if board[i][0] == 'O':
                q.append([i, 0])
                vis.add((i, 0))
                grid[i][0] = 1
            if board[i][m - 1] == 'O':
                q.append([i, m - 1])
                vis.add((i, m - 1))
                grid[i][m - 1] = 1
        for j in range(1, m - 1):
            if board[0][j] == 'O':
                q.append([0, j])
                vis.add((0, j))
                grid[0][j] = 1
            if board[n - 1][j] == 'O':
                q.append([n - 1, j])
                vis.add((n - 1, j))
                grid[n - 1][j] = 1
        while q:
            k = len(q)
            for c in range(k):
                i, j = q.popleft()

                if check(i + 1, j):
                    q.append([i + 1, j])
                    vis.add((i + 1, j))
                    grid[i + 1][j] = 1         

                if check(i - 1, j):
                    q.append([i - 1, j])
                    vis.add((i - 1, j))
                    grid[i - 1][j] = 1
                
                if check(i, j + 1):
                    q.append([i, j + 1])
                    vis.add((i, j + 1))
                    grid[i][j + 1] = 1
                
                if check(i, j - 1):
                    q.append([i, j - 1])
                    vis.add((i, j - 1))
                    grid[i][j - 1] = 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    board[i][j] = 'X'