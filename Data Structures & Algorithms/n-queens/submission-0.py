class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # backtracking, one by one, try all the possible conditon
        diag_set = set()
        counter_diag = set()
        cols = set()
        res = []

        def dfs(r, curr):
            if r >= n:
                res.append(curr.copy())
                return
            for col in range(n):
                curr_diag = r + col
                curr_counter = r - col
                if col not in cols and curr_diag not in diag_set and curr_counter not in counter_diag:
                    curr.append('.'* col + 'Q' + '.' * (n-col-1))
                    cols.add(col)
                    diag_set.add(curr_diag)
                    counter_diag.add(curr_counter)
                    dfs(r+1, curr)
                    curr.pop()
                    cols.remove(col)
                    diag_set.remove(curr_diag)
                    counter_diag.remove(curr_counter)
                

        dfs(0, [])
        return res
            