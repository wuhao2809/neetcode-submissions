class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # maintain a sliding window, use hashmap
        # O(k * n)

        # use monotonic decreasing stack, front of the stack always has the largest element
        stack = []
        res = []
        for i, num in enumerate(nums):
            # move left pointer
            if i >= k: 
                if nums[i - k] == stack[0]:
                    stack.pop(0)

            while stack and stack[-1] < num:
                stack.pop(-1)
            stack.append(num)            


            if i >= k - 1:
                res.append(stack[0])
        return res
                    
        