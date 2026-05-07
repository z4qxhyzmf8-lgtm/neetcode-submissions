class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        #special cases
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1 + (s[0] != s[1])
        l = 0
        r = 1

        #initialising dictionary and removing prefix duplicates
        dict = {s[l] : 1}
        while r < n and s[l] == s[r]:
            l += 1
            r += 1
        ans = len(dict)

        #sliding the window to find substring max length
        while r < n:
            while r < n and dict.get(s[r], 0) == 0:
                dict[s[r]] = 1
                r += 1
            ans = max(ans, len(dict))
            while l < r and r < n and s[l] != s[r]:
                if s[l] in dict:
                    dict.pop(s[l])
                l += 1
                
            l += 1
            r += 1
            
            
            
        return ans
            
        