class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs, mark as 0
        if not grid:
            return 0

        res = 0
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r,c):
            nonlocal grid
            # init is "1"
            grid[r][c] = "0"
            for dire in directions:
                nr = r + dire[0]
                nc = c + dire[1]
                
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == "1":
                    dfs(nr,nc)
            return
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r,c)
        return res
        