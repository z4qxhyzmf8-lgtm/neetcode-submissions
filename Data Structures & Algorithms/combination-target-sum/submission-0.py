class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        sub = []
        n = len(nums)
        def back(s, i):
            nonlocal sol
            nonlocal sub
            nonlocal n

            if i >= n:
                return
            
            if nums[i] > target:
                return
            
            if s == target:
                sol.append(sub.copy())
                return
            elif s > target:
                return

            for j in range(i, n):
                if nums[j] > target:
                    break
                sub.append(nums[j])
                back(s + nums[j], j)
                sub.pop()
        
        back(0, 0)
        return sol

        