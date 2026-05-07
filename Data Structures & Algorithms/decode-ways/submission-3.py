class Solution:
    def numDecodings(self, s: str) -> int:
        def indicator(s1, s2):
            if s1 == '1':
                return 1
            if s1 == '2' and int(s2) <= 6:
                return 1
            return 0 
        n = len(s)
        #dp[i] = nbr of ways to decode s[:i + 1]
        dp = [0 for i in range(n)]
        if s[0] == '0':
            return 0
        
        if n == 1:
            return 1
        
        dp[0] = 1
        if s[1] != '0':
            dp[1] = dp[0] + indicator(s[0], s[1])
        else:
            if int(s[0]) <= 2:
                dp[1] = 1
            else:
                return 0
        for i in range(2, n):
            if s[i] != '0':
                dp[i] = dp[i - 1] + dp[i - 2] * indicator(s[i - 1], s[i])
            else:
                if 0 < int(s[i - 1]) <= 2:
                    dp[i] = dp[i - 2]
                else:
                    return 0
        return dp[n - 1]
            

        
            
        return dp[n - 1] 
        