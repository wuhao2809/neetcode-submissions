class Solution:
    def rob(self, nums: List[int]) -> int:
        # how to do in a circular structure
        # problem is in the last index, if it's robbed, we have to ensure the first and second last are all not robbed; 
        # if we do not rob the first house, or we do not rob the second house
        if len(nums) == 1:
            return nums[0]
        def helper(arr):
            n = len(arr)
            memo = [[0,0] for _ in range(n)]            
            memo[0] = [arr[0], 0]
            for i in range(1, n):
                memo[i][0] = memo[i-1][1] + arr[i]
                memo[i][1] = max(memo[i-1][0], memo[i-1][1])
            return max(memo[-1])
        return max(helper(nums[1:]), helper(nums[:len(nums)-1]))