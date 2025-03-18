# Questions to ask:
# 1. What is the time complexity? O(numCourses + len(prerequisites))
# 2. What is the space complexity? O(numCourses + len(prerequisites))
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for second, first in prerequisites:
            graph[first].append(second)

        states = [0] * numCourses # 0: not visited; 1: visiting; 2: visited

        def dfs(course: int):
            if states[course] == 1: # Cycle detected
                return False
            if states[course] == 2: # Already visited
                return True
            # Mark as visiting
            states[course] = 1
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            # Mark as visited
            states[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

# Problem 207
# Link: https://leetcode.com/problems/course-schedule/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    cases = [
        (2, [[1,0]], True),
        (2, [[1,0], [0,1]], False),
        (3, [[1,0],[2,1],[0,2]], False),
        (5, [[1,4],[2,4],[3,1],[3,2]], True),
    ]
    for numCourses, prerequisites, expected in cases:
        assert s.canFinish(numCourses, prerequisites) == expected
