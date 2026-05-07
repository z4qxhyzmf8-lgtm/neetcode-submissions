class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)
        if n2 > n1:
            return ''

        #compute freq of t
        freq_t = {}

        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1
        

        #slide window to the right until we have the same freq
        #as t; then slide to the left while the window still 
        #contains all elements of s. record this as a possible answer
        #then look at remaing string in the same way

        ans = s
        ok = 0
        freq_s = {}
        l = 0
        count = 0
        for r in range(n1):
            #compute freq of window and compare with freq of t
            freq_s[s[r]] = freq_s.get(s[r], 0) + 1
            if freq_s[s[r]] == freq_t.get(s[r], 0):
                count += 1

            #close window as much as possible then record ans
            if count == len(freq_t):
                
                while freq_s[s[l]] > freq_t.get(s[l], 0):
                    freq_s[s[l]] -= 1
                    l += 1
                if len(s[l: r + 1]) <= len(ans):
                    ok = 1
                    ans = s[l: r + 1]

                
                freq_s[s[l]] -= 1
                l += 1
                count -= 1

        if ok:
            return ans
        return ''


        