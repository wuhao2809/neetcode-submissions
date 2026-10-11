class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # maintain a cursor, then move -> col + , row + , col - , row -
        # use a seen[]
        seen = set()
        rows = len(matrix)
        cols = len(matrix[0])
        
        dires = [(0, 1), (1,0), (0, -1), (-1, 0)]
        curr_dire = 0
        res = []

        r,c = 0,0
        seen.add((0,0))
        while len(seen) < rows * cols:
            res.append(matrix[r][c])
            nr, nc = r + dires[curr_dire][0], c + dires[curr_dire][1]
            if 0<=nr<rows and 0<=nc<cols and (nr, nc) not in seen:
                r,c = nr, nc
            else:
                curr_dire = (curr_dire + 1)%4
                r, c = r + dires[curr_dire][0], c + dires[curr_dire][1]
            seen.add((r,c))
        res.append(matrix[r][c])
        return res