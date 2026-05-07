class Solution:
    def countSubstrings(self, s: str) -> int:
        #O(n^2) idea using dp
        #first idea is dp[i][j] = 1 if s[i:j + 1] is palidrome
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for k in range(1, n):
            for i in range(n - k):
                if s[i] == s[k + i]:
                    if dp[i + 1][k + i - 1] or k <= 2:
                        dp[i][k + i] = 1
        count = 0
        for k in range(n):
            for i in range(n - k):
                if dp[i][k + i]:
                    count += 1
        return count
