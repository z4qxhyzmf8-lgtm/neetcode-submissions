class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp[i] = min coins needed to make amount i
        

        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        #for i in range(coins[0], amount + 1, coins[0]):
        #    dp[i] = i // coins[0]
        
        
        for i in range(len(coins)):
            if coins[i] > amount:
                continue
            dp[coins[i]] = 1
            for j in range(coins[i] + 1, amount + 1):
                max_coins = j // coins[i]
                remainder = j % coins[i]
                for k in range(max_coins + 1):
                    dp[j] = min(dp[j], k + dp[(max_coins - k) * coins[i] + remainder])
            


      
        if dp[amount] < float('inf'):
            return dp[amount]
        return -1





        