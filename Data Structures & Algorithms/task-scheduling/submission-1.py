class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxheap = [-count for count in freq.values()]
        heapq.heapify(maxheap)

        res = 0

        while maxheap:
            pending = []
            executed = 0

            for _ in range(n + 1):
                if not maxheap:
                    break

                count = heapq.heappop(maxheap)
                count += 1  # 负数频率向 0 靠近，表示执行一次
                executed += 1

                if count < 0:
                    pending.append(count)

            # 本轮结束后才能放回，避免同一轮重复执行相同任务
            for count in pending:
                heapq.heappush(maxheap, count)

            if maxheap:
                res += n + 1  # 还有任务，补齐本轮的 idle
            else:
                res += executed  # 最后一轮不用补 idle

        return res