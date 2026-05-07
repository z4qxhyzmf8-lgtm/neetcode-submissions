class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for char in s:
            dict[char] = dict.get(char, 0) + 1
        for char in t:
            if dict.get(char, 0) == 0:
                return False
            else:
                dict[char] -= 1
        for char in s:
            if dict.get(char) != 0:
                return False 
                
                
        return True