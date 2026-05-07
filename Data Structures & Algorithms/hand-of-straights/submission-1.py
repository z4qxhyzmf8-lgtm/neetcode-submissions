class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False
        hand.sort()
        used = [False for _ in range(n)]
        def binary(target, arr):
            nonlocal used
            l, r = 0, len(arr) - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == target and not used[mid]:
                    ans = mid
                    r = mid - 1
                elif arr[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return ans
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            
            for j in range(1, groupSize):
                target = hand[i] + j
                index = binary(target, hand)
                if index == -1:
                    
                    return False
                used[index] = True
        return True 
                


        