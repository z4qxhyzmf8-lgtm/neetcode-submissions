class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        sub = []
        nums = candidates
        nums.sort()
        n = len(nums)

        def back(s, i):
            nonlocal sol
            nonlocal sub
            nonlocal n
            nonlocal nums

            if s == target:
                sol.append(sub.copy())
                return
            j = i + 1
            while j < n:
                if s + nums[j] > target:
                    return 
                sub.append(nums[j])
                back(s + nums[j], j)
                sub.pop()
                j += 1
                while j < n and nums[j] == nums[j - 1]:
                    j += 1
        back(0, -1)
        return sol
        