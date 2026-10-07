class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # income edge
        indegree = [0] * numCourses
        # build the graph
        graph = [[] for _ in range(numCourses)]
        for dst, src in prerequisites:
            indegree[dst] += 1
            graph[src].append(dst)
        
        nodes = deque()
        for i,node in enumerate(indegree):
            if node == 0:
                nodes.append(i)
        
        while nodes:
            curr = nodes.popleft()
            for dst in graph[curr]:
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    nodes.append(dst)
        
        return sum(indegree) == 0
            
        
        
        
        