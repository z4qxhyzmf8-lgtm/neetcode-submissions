class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        #dp[i] = max_sum of subbaray of nums[:i + 1]
        dp = [-float('inf') for _ in nums]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)    
        