class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # dp[start][end] -> dp[start + 1][end - 1]
        n = len(s)
        dp = [[False] * (n) for _ in range(n)]
        res = []
        for i in range(n):
            dp[i][i] = True
        
        for length in range(1, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                dp[start][end] = (
                    s[start] == s[end]
                    and (length <= 2 or dp[start + 1][end - 1])
                )

        res = []
        curr = []
        def dfs(start, curr):
            if start >= n:
                res.append(curr.copy())
                return
            
            for end in range(start, n):
                if dp[start][end]:
                    curr.append(s[start: end+1])
                    dfs(end + 1, curr)
                    curr.pop()
        dfs(0, [])
        return res
