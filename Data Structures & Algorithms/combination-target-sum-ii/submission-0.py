class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking, sorting
        # for a series of identic al number,pick (0-n) of them, 
        n = len(candidates)
        res = []
        candidates.sort()
        # for every step
        def backtrack(curr_res, idx, target):
            if target == 0:
                res.append(curr_res.copy())
                return
            if target < 0 or idx >= n:
                return
            
            # pick the curr
            curr_res.append(candidates[idx])
            backtrack(curr_res, idx + 1, target - candidates[idx])
            curr_res.pop()

            # skip to next val
            while idx < n - 1 and candidates[idx] == candidates[idx + 1]:
                idx += 1
            backtrack(curr_res, idx + 1, target)

            return
        backtrack([], 0, target)
        return res
                