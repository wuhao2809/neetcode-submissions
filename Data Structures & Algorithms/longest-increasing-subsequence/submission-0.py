import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # mono stack? [1,4,4,2,7] no 
        # dp[]
        curr = [nums[0]]
        for num in nums:
            if num > curr[-1]:
                curr.append(num)
                continue
            idx = bisect.bisect_left(curr, num)
            curr[idx] = num
        return len(curr)
        
        