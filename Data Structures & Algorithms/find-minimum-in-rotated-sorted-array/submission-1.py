class Solution:
    def findMin(self, nums: List[int]) -> int:
        #if array is rotated k times, min = nums[k]
        #binary search the number of rotations of the array
        n = len(nums)
        l = 0
        r = n - 1
        ans = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break
            mid = (l + r) // 2
            ans = min(ans, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return ans

        