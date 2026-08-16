class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # build a func so that can use bin search, transform matrix to int
        rows = len(matrix)
        cols = len(matrix[0])
        def trans_to_matrix(idx: int):
            row = idx // (cols)
            col = idx % cols
            return row, col
        left = 0
        right = rows * cols - 1
        while left <= right:
            mid = (left + right)//2
            row, col = trans_to_matrix(mid)
            curr = matrix[row][col]
            if curr == target:
                return True
            elif curr < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
            
        