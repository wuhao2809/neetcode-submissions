class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        def expand(start,end):
            nonlocal res
            while (0<=start<n and 0<=end<n and start <= end and s[start] == s[end]):
                res += 1
                start -= 1
                end += 1
        for i in range(n):
            expand(i,i)
            expand(i,i+1)
        return res