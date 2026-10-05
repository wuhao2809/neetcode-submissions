class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # list all the possibilities
        # use back tracking, choose a start and then choose the next num
        # for the next num, in case of duplicated, only choose idx later than curr
        # after each iteration, pop the num
        res = []
        def getSum(curr_nums, curr_sum, curr_idx):
            nonlocal target
            nonlocal nums
            # base case
            if curr_sum == target:
                res.append(curr_nums.copy())
                return
            
            if curr_sum > target:
                return
            
            # recursive case
            for i in range(curr_idx, len(nums)):
                curr_num = nums[i]
                next_sum = curr_sum + curr_num
                curr_nums.append(curr_num)
                getSum(curr_nums, next_sum, i)
                curr_nums.pop()
            return
        getSum([], 0, 0)
        return res
        