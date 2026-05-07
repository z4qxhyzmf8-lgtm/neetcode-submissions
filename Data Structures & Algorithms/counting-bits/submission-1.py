class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        pow2 = 1
        for i in range(1, n + 1):
            if i == 2 * pow2:
                dp[i] = 1
                pow2 = i
            else:
                dp[i] = 1 + dp[i - pow2]
        return dp
        