class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n2 < n1:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
        n = n1 + n2
        half = n // 2 
        
        l, r = 0, n1 - 1
        while True:
            cut1 = (l + r) // 2
            cut2 = half - cut1 - 2

            left1 = nums1[cut1] if cut1 >= 0 else float('-inf')
            right1 = nums1[cut1 + 1] if (cut1 + 1) < n1 else float('inf')
            left2 = nums2[cut2] if cut2 >= 0 else float('-inf')
            right2 = nums2[cut2 + 1] if (cut2 + 1) < n2 else float('inf')
            print(nums1)
            if left1 <= right2 and left2 <= right1:
                if n % 2:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                r = cut1 - 1
            else:
                l = cut1 + 1
            
            

            

        
        


        