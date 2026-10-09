class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # traverse each element, compare curr_product and res_product, update res_product
        # when to restart the starting point of curr? if curr > curr_product, we can restart from curr. No. Why? because a negative large value is also valuable. 
        # dp, largest positive, smallest negative, 
        # if curr > curr_positive, then restart from curr
        # if curr is negative and curr < curr_negative, negative restart from curr
        # O(n)
        res = nums[0]
        curr_positive = 1
        curr_negative = 1
        for num in nums:
            prev_positive = curr_positive
            prev_negative = curr_negative
            curr_positive = max(num, num*prev_positive, num*prev_negative)
            curr_negative = min(num, num*prev_positive, num*prev_negative)
            res = max(res, curr_positive, curr_negative)
        return res
