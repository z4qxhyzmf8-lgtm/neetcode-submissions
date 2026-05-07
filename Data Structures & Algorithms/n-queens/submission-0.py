class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        sol = []

        def back(i, cols, diag1, diag2):
            nonlocal board
            nonlocal sol

            if i >= n:
                temp = []
                for j in range(n):
                    temp.append(''.join(board[j]))
                sol.append(temp)
                return
        
            for j in range(n):
                if j not in cols and i + j not in diag1 and i - j not in diag2:
                    board[i][j] = 'Q'
                    cols[j] = 1
                    diag1[i + j] = 1
                    diag2[i - j] = 1

                    back(i + 1, cols, diag1, diag2)

                    del cols[j]
                    del diag1[i + j]
                    del diag2[i - j]
                    board[i][j] = '.'
            return 

        back(0, {}, {}, {})
        return sol     

        