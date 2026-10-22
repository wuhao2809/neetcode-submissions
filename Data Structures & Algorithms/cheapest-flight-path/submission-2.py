class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bellman ford
        dist = [float('inf')] * n
        dist[src] = 0
        for _ in range(k+1):
            next_dist = dist.copy()
            for start, end, price in flights:
                if dist[start] != float('inf'):
                    next_dist[end] = min(next_dist[end], dist[start] + price)
            dist = next_dist
        return dist[dst] if dist[dst] != float('inf') else -1