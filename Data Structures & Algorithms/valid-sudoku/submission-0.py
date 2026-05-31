class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    # create three dict, one row, one column, one block
        rows_dict = defaultdict(set)
        cols_dict = defaultdict(set)
        blocks_dict = defaultdict(set)
        for row in range(9):
            for col in range(9):
                curr = board[row][col]
                block_num = self.transferToBlockNum(row,col)
                if curr in rows_dict[row] or curr in cols_dict[col] or curr in blocks_dict[block_num]:
                    return False
                if curr == '.':
                    continue
                rows_dict[row].add(curr)
                cols_dict[col].add(curr)
                blocks_dict[block_num].add(curr)
        return True
            
    
    def transferToBlockNum(self, row, col) -> int:
        return row//3 * 3 + col // 3
        