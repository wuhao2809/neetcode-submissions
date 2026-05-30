class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # two arrays, left_product, right_product, both exclude the current value
        n = len(nums)
        left_product = [1] * n
        right_product = [1] * n
        # left product
        for i in range(1, n):
            left_product[i] = left_product[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            right_product[i] = right_product[i+1] * nums[i+1]
        
        res = []
        for i in range(n):
            res.append(left_product[i] * right_product[i])
        return res