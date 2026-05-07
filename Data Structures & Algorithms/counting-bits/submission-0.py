class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
    
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        pow2 = 1
        for i in range(1, n + 1):
            if i == pow2:
                dp[i] = 1
                pow2 *= 2
            else:
                dp[i] = 1 + dp[i - pow2 // 2]
        return dp
        