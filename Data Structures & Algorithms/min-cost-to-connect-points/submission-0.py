class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        best = [float('inf')] * n
        best[0] = 0
        res = 0
        visited = [False] * n

        for _ in range(n):
            # pick the next node
            nxt = -1
            for i in range(n):
                if not visited[i] and (nxt == -1 or best[i] < best[nxt]):
                    nxt = i
            
            # add to visited
            visited[nxt] = True
            res += best[nxt]

            # update best
            for v in range(n):
                if not visited[v]:
                    next_best = abs(points[nxt][0] - points[v][0]) + abs(points[nxt][1] - points[v][1])
                    if next_best < best[v]:
                        best[v] = next_best
        return res