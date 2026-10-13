class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # topological sort
        graph = defaultdict(set)
        indegree = {}

        # 1. Initialize every unique character
        for word in words:
            for ch in word:
                indegree[ch] = 0

        # 2. Build ordering constraints
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            # Invalid prefix case
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            # Find first different character
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break

        # 3. Topological sort
        queue = deque()

        for ch in indegree:
            if indegree[ch] == 0:
                queue.append(ch)

        res = []

        while queue:
            ch = queue.popleft()
            res.append(ch)

            for nei in graph[ch]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        # 4. Cycle means invalid ordering
        if len(res) != len(indegree):
            return ""

        return "".join(res)