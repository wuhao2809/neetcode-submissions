class Solution:
    def rob(self, nums: List[int]) -> int:
        # max for rob the current, max for not rob the current, 
        n = len(nums)
        memo = [[0, 0] for _ in range(n)]
        memo[0] = [nums[0], 0]
        for i in range(1, n):
            memo[i][0] = nums[i] + memo[i-1][1]
            memo[i][1] = max(memo[i-1][0], memo[i-1][1])
        return max(memo[-1])