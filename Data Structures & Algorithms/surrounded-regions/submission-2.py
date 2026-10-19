class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(r, c):
            board[r][c] = '#'  # 进入时就标记

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and board[nr][nc] == 'O'
                ):
                    dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if (
                    (r == 0 or r == rows - 1 or c == 0 or c == cols - 1)
                    and board[r][c] == 'O'
                ):
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'