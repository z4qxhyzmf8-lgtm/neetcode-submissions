class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dict = {}
        for num in nums:
            if num in dict:
                continue
            else:
                dict[num] = 1

        for key in dict:
            current = key
            while current + 1 in dict:
                dict[key] += 1
                current += 1
        
        longest = 0
        for key in dict:
            longest = max(longest, dict[key])
        
        return longest

        