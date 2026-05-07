class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = ''
        for s in strs:
            n = len(s)
            sol += str(n) + '.' + s
        return sol
            

    def decode(self, s: str) -> List[str]:
        sol = []
        n = len(s)
        i = 0 
        while i < n:
            c = ''
            while i < n and s[i] != '.':
                c += s[i]
                i += 1
            m = int(c)
            i += 1
            word = ''
            while m:
                word += s[i]
                i += 1
                m -= 1
            sol.append(word)
        return sol

