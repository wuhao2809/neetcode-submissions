# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # maxPath(node) -> return the largest value ;maxpath contain curr node with both side, update res, return the value contain the currnode but only one side
        res = float('-inf')
        def maxPath(node) -> int:
            nonlocal res
            if not node:
                return 0
            
            curr = node.val
            # get the max from left and right
            left = maxPath(node.left)
            right = maxPath(node.right)

            res = max(res, curr, curr + left, curr + right, curr + left + right)
            return max(curr, curr+left, curr+right)
        maxPath(root)
        return res
            

        