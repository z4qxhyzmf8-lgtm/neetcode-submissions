class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        dict_l = {}
        dict_c = {}
        dict_s = {}
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    x = int(board[i][j])
                    y_l = (x , i)
                    y_c = (x , j)
                    s = (i // 3) * 3 + j // 3
                    y_s = (x , s)
                    if y_l in dict_l:
                        return False
                    else:
                        dict_l[y_l] = 1

                    if y_c in dict_c:
                        return False
                    else:
                        dict_c[y_c] = 1

                    if y_s in dict_s:
                        return False
                    else:
                        dict_s[y_s] = 1
        return True
                    

        