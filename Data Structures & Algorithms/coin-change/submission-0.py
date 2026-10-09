class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # backtracking, dfs(start_idx, remain) -> calculate every possibility, Time(!)
        # dp[amount] = dp[amount - coin] + 1, if dp[amount] has a value
        # dp[0] = 0, others are None, for each amount, we only take the min
        # Time: O(amount * n_coins), Space: O(amount)
        n = amount + 1
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(1, n):
            for coin in coins:
                if i - coin >= 0 and dp[i-coin]!= float('inf'):
                    dp[i] = min(dp[i-coin] + 1, dp[i])
        return dp[-1] if dp[-1] != float('inf') else -1
        