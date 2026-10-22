class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0:1}
        for num in nums:
            next_dp = defaultdict(int)
            for total, ways in dp.items():
                next_dp[total + num] += ways
                next_dp[total-num] += ways
            dp = next_dp
        return dp[target]