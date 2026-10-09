class Solution:
    def longestPalindrome(self, s: str) -> str:
        # start and end, 
        # if s[start: end] is palindrome, then s[start+1, end-1] is also palindrome
        # len == 1 and len == 2 we can initialized
        # for a loop, we iterate the len range(3, len(n))
        # every time we find a palindrome, we update the res
        
        if len(s) == 1:
            return s
        
        # if len(s) == 2:
            
        res_len = 1
        res_start = 0
        n = len(s)
        memo = [[False] * n for _ in range(n)]
        # init - iterate on the index
        for i in range(n):
            memo[i][i] = True
        # loop
        for l in range(2, n + 1):
            for start in range(n - l + 1):
                end = start + l - 1
                if (memo[start + 1][end - 1] or l == 2) and s[start] == s[end]:
                    memo[start][end] = True
                    if l > res_len:
                        res_len = l
                        res_start = start
        return s[res_start : res_start + res_len]

                