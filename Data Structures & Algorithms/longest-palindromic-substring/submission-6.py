class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_start = 0
        res_end = 0
        n = len(s)
        def expand(start, end):
            nonlocal res_start
            nonlocal res_end
            while (0<=start<n and 0<=end<n and start<=end and s[start] == s[end]):
                if (end - start + 1) > (res_end - res_start + 1):
                    res_start = start
                    res_end = end
                start -= 1
                end += 1
        for i in range(n):
            expand(i,i)
            expand(i,i+1)
        return s[res_start:res_end+1]
                
        