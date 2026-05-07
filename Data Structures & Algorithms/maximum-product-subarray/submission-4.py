class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #suffix and prefix solution
        n = len(nums)
        pref, suff, ans = 1, 1, nums[0]
        for i in range(n):
            
            pref = nums[i] * (pref or 1)
            suff = nums[n - 1 - i] * (suff or 1)
            ans = max(ans, suff, pref)
            
        return ans
        