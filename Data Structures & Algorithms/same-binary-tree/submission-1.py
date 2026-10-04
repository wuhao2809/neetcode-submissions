# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # generate the preorder traversal array
        # if they are the same, then these two trees are identical
        def dfs(root, array):
            if root is None:
                array.append("None")
                return
            dfs(root.left, array)
            dfs(root.right, array)
            array.append(root.val)
            return
        left_array = []
        right_array = []
        dfs(p, left_array)
        dfs(q, right_array)
        return left_array == right_array