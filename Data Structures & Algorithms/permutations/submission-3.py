class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        n = len(nums)

        def back(i, arr):
            nonlocal sol
            nonlocal n
            
            if i == n:
                sol.append(arr.copy())
                return

            for j in range(i, n):
                arr[i], arr[j] = arr[j], arr[i]
                back(i + 1, arr)
                arr[i], arr[j] = arr[j], arr[i]

        back(0, nums)
        return sol

        