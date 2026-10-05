class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = [False] * len(nums)
        reachable[0] = True
        for i, num in enumerate(nums):
            if not reachable[i]:
                continue
            for next_range in range(num+1):
                if i + next_range >= len(nums) - 1:
                    return True
                reachable[i + next_range] = True
        return False
            