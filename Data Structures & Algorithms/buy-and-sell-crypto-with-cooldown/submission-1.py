class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[i][s] = max profit from first i days if we end 
        #           day i in state s; s=0 -> holding
        #           s=1 -> on cd and s=2 -> free to buy
        dp = [[0, 0, 0] for _ in prices]
        for i in range(1, len(prices)):
            #holding
            dp[i][0] = max(dp[i - 1][0] + prices[i] - prices[i - 1], dp[i - 1][2])

            #on cd
            dp[i][1] = prices[i] - prices[i - 1] + dp[i - 1][0]

            #free to buy
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        return max(dp[len(prices) - 1][0], dp[len(prices) - 1][1], dp[len(prices) - 1][2])