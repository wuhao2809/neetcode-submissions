class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # width = right smaller index - left smaller index - 1
        n = len(heights)
        left = [-1] * n
        stack = []
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        stack = []
        ans = 0
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right = stack[-1]
            else:
                right = n
            stack.append(i)
            ans = max(ans, heights[i] * (right - left[i] - 1))
        return ans
            