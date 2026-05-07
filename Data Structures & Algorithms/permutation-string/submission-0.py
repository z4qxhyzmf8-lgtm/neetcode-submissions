class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        freq1 = {}
        freq2 = {}
        for char in s1:
            freq1[char] = freq1.get(char, 0) + 1
        
        l = 0
        r = 0
        count = 0
        for char in s2:
            freq2[char] = freq2.get(char, 0) + 1
            if r - l + 1 > n1:
                if freq1.get(s2[l], 0) == freq2[s2[l]]:
                    count -= 1
                freq2[s2[l]] -= 1
                l += 1
            if freq1.get(char, 0) == freq2[char]:
                count += 1
            if count == len(freq1):
                return True
                
            r += 1
        return False
            
        