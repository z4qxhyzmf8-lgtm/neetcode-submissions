class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #tails[i] = smallest possible ending element for a 
        #LIS of length i + 1
        n = len(nums)
        tails = [nums[0]]
        for i in range(1, n):
            print(tails)
            if tails[-1] < nums[i]:
                tails.append(nums[i])
            else:
                #binary search where to replace in tails
                l, r = 0, len(tails) - 1
                while l <= r:
                    m = (l + r) // 2
                    if tails[m] > nums[i]:
                        r = m - 1
                    elif tails[m] == nums[i]:
                        break
                    else:
                        l = m + 1
                if m == len(tails) - 1:
                    tails[m] = nums[i]
                elif tails[m] < nums[i]:
                    tails[m + 1] = nums[i]
                else:
                    tails[m] = nums[i]
        return len(tails)
        