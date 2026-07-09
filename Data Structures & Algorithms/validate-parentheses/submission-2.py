class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack
        stack = []
        corr_bracket = {"(" : ")", "[":"]", "{" : "}"}
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack or corr_bracket[stack.pop()] != char:
                    return False
        return not stack