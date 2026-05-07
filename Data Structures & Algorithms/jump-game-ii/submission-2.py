class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        jumps = 0
        i = 0
        while i < n:
            jumps += 1
            jump = nums[i]
            if i + jump >= n - 1:
                return jumps
            max_jump = i + nums[i]
            max_index = i + nums[i]
            for j in range(i + 1, i + jump + 1):
                if j + nums[j] >= max_jump:
                    max_jump = j + nums[j]
                    max_index = j
            i = max_index
        return jumps
  
        
        