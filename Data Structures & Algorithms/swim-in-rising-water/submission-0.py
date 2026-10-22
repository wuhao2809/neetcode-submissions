class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # dijkstra
        # heap -> (max_height to this point,r ,c )
        n = len(grid)
        best = [[float('inf')] * n for _ in range(n)]
        best[0][0] = grid[0][0]
        heap = [(grid[0][0], 0, 0)]
        
        dires = [(0,1), (1,0), (-1,0), (0,-1)]
        while heap:
            height, r, c = heapq.heappop(heap)
            
            if best[r][c] != height:
                continue
            
            # early return
            if r == n-1 and c == n-1:
                return height
            
            for dr, dc in dires:
                nr, nc = r + dr, c + dc
                if 0<=nr<n and 0<=nc<n:
                    new_height = max(height, grid[nr][nc])
                    if new_height < best[nr][nc]:
                        best[nr][nc] = new_height
                        heapq.heappush(heap, (new_height, nr, nc))
        return best[-1][-1]
            
            
            
        
        