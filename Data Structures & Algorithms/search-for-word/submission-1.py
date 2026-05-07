class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board) #nr of rows
        m = len(board[0]) #nr of cols
        nw = len(word)

        def back(i, j, k):
            nonlocal n
            nonlocal m
            nonlocal nw

            if k == nw:
                return True

            if i < 0: 
                return False
            if j < 0:
                return False
            if i >= n:
                return False
            if j >= m:
                return False
            if board[i][j] != word[k]:
                return False
            
            board[i][j] = '@'
            ok = (back(i - 1, j, k + 1) or
                  back(i + 1, j, k + 1) or
                  back(i, j - 1, k + 1) or
                  back(i, j + 1, k + 1)
                )
            board[i][j] = word[k]
            return ok

            
        
        for i in range(n):
            for j in range(m):
                if back(i, j, 0):
                    return True
        return False
                
        