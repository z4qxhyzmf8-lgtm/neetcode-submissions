class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        #dp[i][j] = number of ways to achieve a sum of j using
        #           elements up to index i
        dp = [defaultdict() for _ in range(n)]
        dp[0][nums[0]] = dp[0].get(nums[0], 0) + 1
        dp[0][-nums[0]] = dp[0].get(-nums[0], 0) + 1
        partial_sum = nums[0]
        for i in range(1, n):
            for j in range(-partial_sum, partial_sum + 1):
                if dp[i - 1].get(j, 0):
                    dp[i][j + nums[i]] = dp[i].get(j + nums[i], 0) + dp[i - 1][j]
                    dp[i][j - nums[i]] = dp[i].get(j - nums[i], 0) + dp[i - 1][j]
            partial_sum += nums[i]
        print(dp)
        return dp[n - 1].get(target, 0)

        