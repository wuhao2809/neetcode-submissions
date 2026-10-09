class Solution:
    def numDecodings(self, s: str) -> int:
        # decode it one by one, every number should belong to a part of a letter.
        # every one or two digit can form a letter
        # if s[:n-1] == dp[n-2]:
        # if s[n-1] == 0, res_new = dp[n-2]
        # [solo, not solo]
        # dp[i][0] = dp[i-1][0] + dp[i-1][1]
        # dp[i][1] = dp[i-1][0]
        # if not possible to solo or not solo, go 0
        n = len(s)
        dp = [[0, 0] for _ in range(n)]
        if s[0] == "0":
            return 0
        dp[0] = [1, 0]
        for i in range(1,n):
            # solo
            if s[i] != "0":
                dp[i][0] = dp[i-1][0] + dp[i-1][1]
            # not solo
            if s[i-1] != "0" and int(s[i-1:i+1]) <= 26:
                dp[i][1] = dp[i-1][0]
        return sum(dp[-1])
        