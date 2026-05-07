class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #dp[j] = ways to make amount j 
        coins.sort()
        dp = [0 for _ in range(amount + 1)] 
        dp[0] = 1
        for coin in coins:
            if coin > amount:
                break
            dp[coin] += 1
            
            for j in range(coin + 1, amount + 1):
                dp[j] += dp[j - coin]


        return dp[amount]

        



        
        