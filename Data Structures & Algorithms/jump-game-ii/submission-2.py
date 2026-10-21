class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        l = r = 0
        while r < n-1:
            fartherest = r
            while l <= r:
                fartherest = max(fartherest, l + nums[l])
                l += 1
            l = r + 1
            r = fartherest
            res += 1 
        return res
                