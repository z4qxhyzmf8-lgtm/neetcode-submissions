class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        sol = []
        sub = []
        
        def back(i):
            nonlocal sol
            nonlocal n
            nonlocal sub

            sol.append(sub.copy())

            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                sub.append(nums[j])
                back(j + 1)
                sub.pop()
                
            return
        back(0)
        return sol

        