class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #dp[i] = k, such that k in binary represents which elements
        #of nums we need to sum to i
        total = 0
        for num in nums:
            total += num
        if total % 2:
            return False
        half = total // 2
        dp = [0 for _ in range(half + 1)]
        n = len(nums)
        for i in range(n):
            if nums[i] > half:
                return False
            if dp[nums[i]]:
                continue
            dp[nums[i]] ^= (1 << i) 
        
        for s in range(1, half + 1):
            if dp[s]:
                for j in range(n):
                    if s + nums[j] <= half:
                        if dp[s] & (1 << j):
                            continue
                        else:
                            dp[s + nums[j]] = dp[s] ^ (1 << j)
                    if dp[half]:
                        return True
        if dp[half]:
            return True
        return False
        

                

                
        