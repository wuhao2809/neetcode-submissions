class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = ""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build a trie from words
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if not curr.children[ord(char) - ord('a')]:
                    curr.children[ord(char) - ord('a')] = TrieNode()
                curr = curr.children[ord(char) - ord('a')]
            curr.word = word

        # use dfs to traverse, pass the curr pos, seen, and also remember to backtrack, remove from seen
        res = set()
        rows = len(board)
        cols = len(board[0])
        dires = [(1,0), (0,1), (-1,0), (0,-1)]
        def dfs(r, c, seen, node):
            if node.word:
                res.add(node.word)
            
            # for next step, add seen first
            for dire in dires:
                nr = r + dire[0]
                nc = c + dire[1]
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in seen and node.children[ord(board[nr][nc]) - ord('a')]:
                    seen.add((nr,nc))
                    dfs(nr,nc,seen,node.children[ord(board[nr][nc]) - ord('a')])
                    seen.remove((nr,nc))
        # traverse possible start form board
        for r in range(rows):
            for c in range(cols):
                if root.children[ord(board[r][c]) - ord('a')]:
                    dfs(r,c,{(r,c)},root.children[ord(board[r][c]) - ord('a')])
        # return res
        return list(res)