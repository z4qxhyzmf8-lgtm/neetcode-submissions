class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        need_to_reach = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= need_to_reach:
                need_to_reach = i
        return need_to_reach == 0

        