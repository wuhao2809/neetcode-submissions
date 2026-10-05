# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder denote the head
        # what is left and what is right

        # pre: 4,2,1,3,6,5,7
        # inorder: 1,2,3,4,5,6,7

        # divide and conquer
        # build subtree, preorder divide the inorder array, use the preorder index to divide the inorder array, recursion
        inorderIndex = {}
        preorder_idx = 0
        for i, val in enumerate(inorder):
            inorderIndex[val] = i
        def buildSubTree(inorder_start_idx, inorder_end_idx):
            nonlocal preorder_idx
            if inorder_start_idx > inorder_end_idx:
                return None
            root_val = preorder[preorder_idx]
            curr = TreeNode(root_val)
            preorder_idx += 1
            curr.left = buildSubTree(inorder_start_idx, inorderIndex[root_val] - 1)
            curr.right = buildSubTree(inorderIndex[root_val] + 1, inorder_end_idx)
            return curr
        return buildSubTree(0, len(preorder) - 1)
            
        