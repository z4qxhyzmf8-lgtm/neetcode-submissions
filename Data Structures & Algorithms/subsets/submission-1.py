class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #
        #initial backtrack solution, apparently due to tupling
        #it ends up being less effective
        #
        #mp = {(): 1}
        #def back(v):
        #    nonlocal sol
        #    
        #    if tuple(v) not in mp:
        #        mp[tuple(v)] = 1
        #    
        #    n = len(v)
        #    if n == 1 or n == 0:
        #        return
        #    for i in range(n):
        #        if i == 0:
        #            back(tuple(v[1:]))
        #        elif i == n - 1:
        #            back(tuple(v[:n - 1]))
        #        else:
        #            v_left = v[:i]
        #            v_right = v[i + 1:]
        #            back(tuple(v_left + v_right))
        #back(nums)
        #sol = []
        #for key in mp:
        #    sol.append(list(key))
        #return sol
        #
        #effective backtracking
        #
        sol = []
        sub = []
        def back(i):
            nonlocal sol
            nonlocal sub
            if i >= len(nums):
                sol.append(sub.copy())
                return
            sub.append(nums[i])
            back(i + 1)
            sub.pop()
            back(i + 1)
        back(0)
        return sol

        