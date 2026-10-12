class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # LCS - if last element is identical : LCS(t1,t2) = LCS(t1-1, t2-1) + 1
        # else: LCS(t1,t2) = max(LCS(t1, t2-1), LCS(t1-1, t2-1))
        n_t1 = len(text1) # row
        n_t2 = len(text2) # col
        res = 0
        dp = [[0] * (n_t2 + 1) for _ in range(n_t1 + 1)]
        for l1 in range(1, n_t1 + 1):
            for l2 in range(1, n_t2 + 1):
                if text1[l1-1] == text2[l2-1]:
                    dp[l1][l2] = dp[l1-1][l2-1] + 1
                else:
                    dp[l1][l2] = max(dp[l1-1][l2], dp[l1][l2-1])
        return dp[-1][-1]
