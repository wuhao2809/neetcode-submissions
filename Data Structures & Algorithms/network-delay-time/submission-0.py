class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))

        minHeap = [(0, k)]
        visited = set()

        max_time = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            max_time = time

            for nei, weight in graph[node]:
                if nei not in visited:
                    heapq.heappush(
                        minHeap,
                        (time + weight, nei)
                    )

        if len(visited) == n:
            return max_time

        return -1