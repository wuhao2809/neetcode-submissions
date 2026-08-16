class Solution:
    def findMin(self, nums: List[int]) -> int:
        # left, mid, right
        # if mid > right, that means it's on right of mid,
        # if it's smaller, than it's on the left
        # update ans = min(ans, mid) everytime
        n = len(nums)
        l, r = 0, n - 1
        ans = float('inf')
        while l <= r:
            mid = (l + r) // 2
            ans = min(nums[mid], ans)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return ans