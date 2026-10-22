from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        @cache
        def dfs(r, c):
            best = 1  # 只包含当前格子

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and 0 <= nc < cols
                        and matrix[nr][nc] > matrix[r][c]):
                    best = max(best, 1 + dfs(nr, nc))

            return best

        return max(dfs(r, c) for r in range(rows) for c in range(cols))