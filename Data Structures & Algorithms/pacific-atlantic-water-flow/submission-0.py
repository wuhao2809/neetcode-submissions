class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # check every cell, traverse every paths, see if it can go to both; use a seen to keep track of all the paths, 
        rows = len(heights)
        cols = len(heights[0])
        # [pacific, atlantic]
        memo = [[[False, False] for _ in range(cols)] for _ in range(rows)]
        # for i in range(rows):
        #     memo[i][0][0] = True
        #     memo[i][cols-1][1] = True
        
        # for i in range(cols):
        #     memo[0][i][0] = True
        #     memo[rows-1][i][1] = True

        # one at a time, dire can only be 0 or 1
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        def bfs(r, c, dire):
            # only change the status that is higher than curr
            # (r,c)
            nodes = deque([(r,c)])
            while nodes:
                for _ in range(len(nodes)):
                    curr_r, curr_c = nodes.popleft()
                    # check the memo
                    if memo[curr_r][curr_c][dire]:
                        continue

                    # assign the memo
                    memo[curr_r][curr_c][dire] = True
                    # move on to next
                    for dires in directions:
                        nr, nc = curr_r + dires[0], curr_c + dires[1]
                        if 0<=nr<rows and 0<=nc<cols and heights[curr_r][curr_c] <= heights[nr][nc]:
                            nodes.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                # only traverse the edge
                if r == 0 or c == 0:
                    bfs(r,c,0)
                if r == rows - 1 or c == cols - 1:
                    bfs(r,c,1)
        
        # append res
        res = []
        for r in range(rows):
            for c in range(cols):
                if memo[r][c][0] and memo[r][c][1]:
                    res.append([r,c])
        return res

                
