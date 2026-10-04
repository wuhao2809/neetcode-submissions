# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # check if curr node can be start of subtree
        
        if self.sameTree(root, subRoot):
            return True
        
        if not root and not subRoot:
            return True
        
        if root:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False

        # check if curr the two tree starting at curr node is the same
    def sameTree(self, root, subRoot):
        # base
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        
        return False