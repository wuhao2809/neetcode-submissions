class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_stack = []
        n = len(temperatures)
        # mono decreasing stack
        # back to front
        res = []
        stack = []
        for i in range(n-1, -1, -1):
            curr = temperatures[i]
            while stack and stack[-1][0] <= curr:
                stack.pop()
            stack.append((curr, i))
            if len(stack) == 1:
                res.append(0)
            else:
                res.append(stack[-2][1] - i)
        return res[::-1]

        # reverse the res
        
        