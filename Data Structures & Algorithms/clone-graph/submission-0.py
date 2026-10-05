"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        seen = {}
        def cloneNode(node):
            nonlocal seen
            if not node:
                return
            
            if node in seen:
                return seen[node]
            
            seen[node] = Node(node.val)
            for neighbor in node.neighbors:
                seen[node].neighbors.append(cloneNode(neighbor))
            return seen[node]
        return cloneNode(node)

