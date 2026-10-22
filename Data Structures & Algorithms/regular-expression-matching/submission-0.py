from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j):
            if j == len(p):
                return i == len(s)

            first_match = (
                i < len(s)
                and (p[j] == s[i] or p[j] == '.')
            )

            if j + 1 < len(p) and p[j + 1] == '*':
                return (
                    dfs(i, j + 2)                  # x* 匹配零个字符
                    or (first_match and dfs(i + 1, j))  # 匹配一个，继续留在 x*
                )

            return first_match and dfs(i + 1, j + 1)

        return dfs(0, 0)