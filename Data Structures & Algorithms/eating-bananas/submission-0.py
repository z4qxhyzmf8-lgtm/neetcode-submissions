class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_p = 0
        for pile in piles:
            max_p = max(max_p, pile)
        
        l = 1
        r = max_p
        k = max_p
        while l <= r:
            mid = (l + r) // 2
            count = 0
            for pile in piles:
                count += pile // mid + (pile % mid != 0)
            if count > h:
                l = mid + 1
            else:
                r = mid - 1
                k = min(k, mid)
        return k


        