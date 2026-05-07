class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []

        def back(sub, arr):
            nonlocal sol
            
            if len(arr) == 1:
                sol.append(arr)
                return
            if len(arr) == 2:
                sub.append(arr[0])
                sub.append(arr[1])
                sol.append(sub.copy())
                sub.pop()
                sub.pop()

                sub.append(arr[1])
                sub.append(arr[0])
                sol.append(sub.copy())
                sub.pop()
                sub.pop()
                return
            n = len(arr)
            for i in range(n):
                sub.append(arr[i])
                if i == 0:
                    v = arr[1:]
                elif i == n - 1:
                    v = arr[:n - 1]
                else:
                    v1 = arr[:i]
                    v2 = arr[i + 1:]
                    v = v1 + v2
                back(sub, v) 
                sub.pop()
        back([], nums)
        
        return sol

        