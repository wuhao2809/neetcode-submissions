class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        res = 0
        # build the graph, adj list
        graph = [[] for _ in range(n)]
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        for i in range(n):
            if i in visited:
                continue
            
            visited.add(i)
            res += 1
            nodes = deque()
            nodes.append(i)
            while nodes:
                curr = nodes.popleft()
                visited.add(curr)
                neighbors = graph[curr]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        nodes.append(neighbor)
        return res
            
                
        