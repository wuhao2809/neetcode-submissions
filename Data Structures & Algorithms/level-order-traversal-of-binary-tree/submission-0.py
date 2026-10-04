# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        if not root:
            return []
        res = []
        layer = deque([root])
        while layer:
            # copy the layer
            curr_res = [node.val for node in layer]
            res.append(curr_res)
            for i in range(len(layer)):
                curr_node = layer.popleft()
                if curr_node.left:
                    layer.append(curr_node.left)
                
                if curr_node.right:
                    layer.append(curr_node.right)
        
        return res
                
        
        