# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # dfs, preorder, when traversing, use a key to denote the current order
        # bfs, bit hard, layer by layer
        order = 1
        res = -1
        def dfs(node):
            nonlocal order
            nonlocal res
            nonlocal k
            if not node:
                return
            dfs(node.left)
            if res != -1:
                return
            if order == k:
                res = node.val
                return
            
            order += 1
            dfs(node.right)
        dfs(root)
        return res
        
        