from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # only keep the nearest and largest integer
        # scan from right to left
        # (value, index)
        n = len(temperatures)
        stack = []
        result = deque()
        for i in range(n-1, -1, -1):
            curr = temperatures[i]
            # judge the result
            found = False
            for j in range(len(stack)-1, -1, -1):
                if stack[j][0] > curr:
                    result.appendleft(stack[j][1] - i)
                    found = True
                    break
            if not found:
                result.appendleft(0)

            # modify the stack
            while stack and stack[-1][0] <= curr:
                stack.pop()
            stack.append((curr, i))
        print(stack)
        return list(result)
            