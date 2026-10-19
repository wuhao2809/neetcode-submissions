class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        q = deque()
        fresh_count = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                
                if grid[r][c] == 1:
                    fresh_count += 1
        time = -1
        dires = [(1,0),(0,1),(-1,0),(0,-1)]
        if fresh_count == 0:
            return 0
        while q:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dire in dires:
                    nr, nc = r + dire[0], c + dire[1]
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        q.append((nr,nc))
        return time if fresh_count == 0 else -1
