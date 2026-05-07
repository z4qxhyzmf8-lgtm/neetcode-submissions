class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #count 0's first
        n = len(nums)
        count = 0
        p = 1
        for num in nums:
            if num == 0:
                count += 1
            else:
                p *= num
        if count > 1:
            return [0 for _ in range(n)]
        elif count == 1:
            sol = [0 for _ in range(n)]
            for i, num in enumerate(nums):
                if num == 0:
                    sol[i] = p
            return sol
        
        #we compute the product to the left of the missing entry
        #and to the right of the missing entry independently 
        sol = [1 for _ in range(n)]

        #product to the left
        for i in range(1, n):
            sol[i] = nums[i - 1] * sol[i - 1]
 
        #product to the right
        p = 1
        for i in range(1, n):
            p *= nums[n - i]
            sol[n - 1 - i] *= p
        return sol
        
        