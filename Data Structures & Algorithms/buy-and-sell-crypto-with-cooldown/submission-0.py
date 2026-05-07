class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[i][c] = max profit we can acheive in first i days
        #           if we are on cd on day i (c = 1), or not (c=0)
        dp = [[-float('inf'), -float('inf')] for _ in prices] 
        dp[0][0] = 0
        dp[0][1] = 0
        for i in range(1, len(prices)):
            #not on cd
            dp[i][0] = max(dp[i - 1][0] + prices[i] - prices[i - 1], dp[i - 1][1])

            #on cd
            dp[i][1] = dp[i - 1][0]

        return max(dp[len(prices) - 1][0], dp[len(prices) - 1][1]) 