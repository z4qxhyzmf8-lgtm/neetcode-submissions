class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sol = []
        sub = []
        n = len(s)


        def check(s):
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def back(i):
            nonlocal sol
            nonlocal sub
            nonlocal n

            if i >= n:
                sol.append(sub.copy())
                return
            
            for j in range(i, n):
                if check(s[i: j + 1]):
                    sub.append(s[i: j + 1])
                    back(j + 1)
                    sub.pop()
                
        
        back(0)
        return sol
        



        

        