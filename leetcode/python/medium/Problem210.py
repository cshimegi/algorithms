# Questions to ask:
# 1. What is the time complexity? O(numCourses + len(prerequisites))
# 2. What is the space complexity? O(numCourses + len(prerequisites))
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for second, first in prerequisites:
            graph[first].append(second)

        states = [0] * numCourses # 0: not visited; 1: visiting; 2: visited
        ans = []

        def dfs(course: int):
            if states[course] == 1:
                return False
            if states[course] == 2:
                return True

            states[course] = 1
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            states[course] = 2
            ans.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return ans[::-1] # because of dfs

# Problem 210
# Link: https://leetcode.com/problems/course-schedule-ii/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    cases = [
        (2, [[1, 0]], [0, 1]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 2, 1, 3]),
        (1, [], [0]),
    ]
    for numCourses, prerequisites, expected in cases:
        assert s.findOrder(numCourses, prerequisites) == expected
