class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(curr, curr_left, total_left):
            if len(curr) == 2*n:
                res.append("".join(curr))
                return
            
            # left
            if total_left < n:
                curr.append('(')
                dfs(curr, curr_left + 1, total_left + 1)
                curr.pop()
            # right
            if curr_left > 0:
                curr.append(')')
                dfs(curr, curr_left - 1, total_left)
                curr.pop()
            return
        dfs([], 0, 0)
        return res