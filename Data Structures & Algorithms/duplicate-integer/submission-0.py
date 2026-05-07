class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            if dict.get(num, 0) != 0:
                return True
            else:
                dict[num] = 1
        return False
        