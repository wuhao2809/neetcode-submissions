# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # bfs: keep track of the parents, this is bst
        curr = root
        while curr:
            # move right
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # move left
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # return
            else:
                return curr