# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # determine if the tree starting from curr node is valid
        def isValidHelper(node, low, high):
            if not node:
                return True
            
            if low<node.val<high:
                return isValidHelper(node.right, max(low, node.val), high) and isValidHelper(node.left, low, min(high, node.val))
            return False
        
        return isValidHelper(root, float('-inf'), float('inf'))
        