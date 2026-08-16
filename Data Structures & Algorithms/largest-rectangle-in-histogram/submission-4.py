class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # width = right smaller index - left smaller index - 1
        # left: mono incrasing, right: mono increasing (remaining elements assigned to n)
        n = len(heights)
        left = [-1] * n
        # default right to n, so we can leave them there in the end
        stack = []
        ans = 0
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                ans = max(ans, heights[stack[-1]] * (i - left[stack[-1]] - 1))
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        for i in stack:
            ans = max(ans, heights[i] * (n - left[i] - 1))
        return ans
            