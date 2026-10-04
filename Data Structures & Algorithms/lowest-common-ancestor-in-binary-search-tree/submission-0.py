# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None
        # dfs, the first matched node have the res, others just break
        def getLCA(node) -> int:
            nonlocal res
            if not node:
                return 0
            if res:
                return 0
            
            matched = 0
            if node.val == p.val:
                matched += 1
            
            if node.val == q.val:
                matched += 1
            
            matched += (getLCA(node.left) + getLCA(node.right))
            if matched == 2 and not res:
                res = node
            return matched
        getLCA(root)
        return res
            