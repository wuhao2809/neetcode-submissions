class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                curr = stack.pop()
                prev = stack.pop()
                res_curr = 0
                if token == "+":
                    res_curr = curr + prev
                elif token == "-":
                    res_curr = prev - curr
                elif token == "*":
                    res_curr = prev * curr
                else:
                    res_curr = int(prev / curr)
                stack.append(res_curr)
            
            else:
                stack.append(int(token))
        return stack[0]