# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder = []
        def dfs(node):
            if not node:
                preorder.append('#')
                return
            preorder.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        return ",".join(preorder)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(',')
        idx = 0
        def build():
            nonlocal idx
            if idx >= len(preorder):
                return
            
            if preorder[idx] == '#':
                idx += 1
                return None
            curr = TreeNode(val=int(preorder[idx]))
            idx += 1
            curr.left = build()
            curr.right = build()
            return curr
        return build()
