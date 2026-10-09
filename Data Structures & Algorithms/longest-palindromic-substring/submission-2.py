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
            
        res = s[0]
        n = len(s)
        memo = [[False] * n for _ in range(n)]
        # init - iterate on the index
        for i in range(n):
            memo[i][i] = True
            if i + 1 < n:
                memo[i][i+1] = (s[i] == s[i+1])
                if memo[i][i+1]:
                    res = s[i:i+2]
        # loop
        for l in range(3, n + 1):
            for start_idx in range(0, n - l + 1):
                end_idx = start_idx + l - 1 
                if memo[start_idx + 1][end_idx - 1] and s[start_idx] == s[end_idx]:
                    memo[start_idx][end_idx] = True
                    if l > len(res):
                        res = s[start_idx:end_idx + 1]

        # return
        return res