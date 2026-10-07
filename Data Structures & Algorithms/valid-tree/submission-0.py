class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # as long as there is no cycle, then it can be formed as a tree
        # determine whether there is a cycle
        # traverse each node, to see if the path can contain a cycle,
        # we need a set seen, and a prev node, as long as curr is in seen or some nodes not visited, then return False, else return True
        # O(n), O(n)
        seen = set()
        nodes = deque()

        # build the graph
        graph = [[] for _ in range(n)]
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        # [curr, prev]
        nodes.append((0, -1))
        while nodes:
            curr, prev = nodes.popleft()
            if curr in seen:
                return False
            else:
                seen.add(curr)
            for dst in graph[curr]:
                if dst != prev:
                    nodes.append((dst,curr))
        return len(seen) == n
                        
        