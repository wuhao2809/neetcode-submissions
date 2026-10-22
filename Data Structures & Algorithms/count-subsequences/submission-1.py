class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 从任意 s 前缀中选出空字符串：只有「一个字符都不选」这一种
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]  # 不选 s[i-1]

                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]  # 选 s[i-1]

        return dp[m][n]