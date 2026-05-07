class Solution:
    def longestPalindrome(self, s: str) -> str:
        #one option is dp[i][j] = 1 if s[i:j+1] is a palindrome
        #n = len(s)
        #   
        #dp = [[0 for _ in range(n)] for _ in range(n)]
        #for i in range(n):
        #    dp[i][i] = 1
        #
        #for k in range(1, n):
        #    for i in range(n - k):
        #        if s[i] == s[k + i]:
        #            if dp[i + 1][k + i - 1] or k <= 2:
        #                dp[i][k + i] = 1
        #ans = 1
        #start_indx = 0
        #end_indx = 0
        #for k in range(n):
        #    for i in range(n - k):
        #        if dp[i][k + i]:
        #            if k + 1 > ans:
        #                ans = k + 1
        #                start_indx = i
        #                end_indx = k + i
        #return s[start_indx: end_indx + 1] 
        #
        #second option with same time complexity but better space
        #is a two pointer approach
        #
        n = len(s)
        left_indx = 0
        length = 0

        for i in range(n):
            #odd case
            l = i
            r = i
            while l >= 0 and r < n and s[l] == s[r]:     
                if r - l + 1 > length:
                    left_index = l
                    length = r - l + 1
                l -= 1
                r += 1

            #even case
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:     
                if r - l + 1 > length:
                    left_index = l
                    length = r - l + 1
                l -= 1
                r += 1
        return s[left_index: length + left_index]


        