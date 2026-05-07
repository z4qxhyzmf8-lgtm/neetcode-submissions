class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #n = len(nums)
        #s = sum(nums)
        #return n * (n + 1) // 2 - s 
        #
        #bit manip solution
        #
        n = len(nums)
        ans = n
        for i in range(n):
            ans ^= i ^ nums[i]
        return ans
        