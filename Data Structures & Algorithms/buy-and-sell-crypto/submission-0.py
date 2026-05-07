class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        if n == 1:
            return 0
        if n == 2:
            return max(prices[1] - prices[0], 0)
        min_price = prices[0]
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit

        
        