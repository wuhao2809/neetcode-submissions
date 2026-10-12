class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # LCS - if last element is identical : LCS(t1,t2) = LCS(t1-1, t2-1) + 1
        # else: LCS(t1,t2) = max(LCS(t1, t2-1), LCS(t1-1, t2-1))
        n_t1 = len(text1) # row
        n_t2 = len(text2) # col
        res = 0
        prev = [0] * (n_t2 + 1)
        curr = [0] * (n_t2 + 1)
        for l1 in range(1, n_t1 + 1):
            for l2 in range(1, n_t2 + 1):
                if text1[l1-1] == text2[l2-1]:
                    curr[l2] = prev[l2-1] + 1
                else:
                    curr[l2] = max(curr[l2-1], prev[l2])
            prev = curr
            curr = [0] * (n_t2 + 1)
        return prev[-1]
