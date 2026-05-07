class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        p = ''

        for i in range(n):
            if s[i] >= 'a' and s[i] <= 'z':
                p += s[i]
            elif s[i] >= 'A' and s[i] <= 'Z':
                p += chr(ord(s[i]) - ord('A') + ord('a')) 
            elif s[i] >= '0' and s[i] <= '9':
                p += s[i]
        
        n = len(p)
        l = 0
        r = n - 1

        while l < r:
            if p[l] == p[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        