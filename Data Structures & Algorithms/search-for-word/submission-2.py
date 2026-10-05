class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # use the idx for word, get each char
        # traverse, dfs or bfs, bfs is better for iteration, dfs is more natural for recursion; use dfs
        # track the path through a list, after sub-dfs return, pop the list
        # boundary condition check before next dfs, save time

        res = False
        if not board:
            return False
        if not word:
            return True

        rows = len(board)
        cols = len(board[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        def dfs(curr_path, curr_idx, curr_pos):
            nonlocal res
            if res:
                return
            
            # curr_idx not judged
            if curr_idx == len(word):
                res = True
                return
            
            # recursive step
            r, c = curr_pos
            for dire in directions:
                next_r = r + dire[0]
                next_c = c + dire[1]
                # boundary check and next idx check
                if 0<=next_r<rows and 0<=next_c<cols and ((next_r, next_c) not in curr_path) and board[next_r][next_c] == word[curr_idx]:
                    # append path
                    curr_path.append((next_r, next_c))
                    # dfs
                    dfs(curr_path, curr_idx + 1, (next_r,next_c))
                    # pop path
                    curr_path.pop()
        
        for r in range(rows):
            for c in range(cols):
                if res:
                    return True
                if board[r][c] == word[0]:
                    dfs([(r,c)], 1, (r,c))

        return res
        