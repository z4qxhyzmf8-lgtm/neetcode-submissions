class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        def back(s, open, close):
            nonlocal sol

            if len(s) == 2 * n:
                sol.append(s)
                return
            
            if open < n:
                back(s + '(', open + 1, close)
            if close < open:
                back(s + ')', open, close + 1)
            
        
        back('', 0, 0)
        return sol


        