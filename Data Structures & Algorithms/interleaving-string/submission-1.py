class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # find the state
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        # row: s1->m, col : s2->n
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True # use i and j elements
        for i in range(m + 1):
            for j in range(n + 1):
                if i > 0 and dp[i-1][j] and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = True
                
                if j > 0 and dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = True
        return dp[-1][-1]
        