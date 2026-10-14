class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # [a, b] means b -> a
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque()

        # 没有 prerequisite 的课可以先上
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        order = []

        while q:
            course = q.popleft()
            order.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    q.append(next_course)

        if len(order) == numCourses:
            return order

        return []