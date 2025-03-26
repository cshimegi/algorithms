# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # Adjacency lists for each vertex
        graph = [[] for _ in range(n)]
        # Initialize adjacency lists with self-loops
        for vertex in range(n):
            graph[vertex] = [vertex]

        # Build adjacency lists from edges
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        # Map to store frequency of each unique adjacency list
        component_freq = defaultdict(int)
        # Count frequency of each unique adjacency pattern
        for vertex in range(n):
            neighbors = tuple(sorted(graph[vertex]))
            component_freq[neighbors] += 1

        # Count complete components where size equals frequency
        return sum(
            1
            for neighbors, freq in component_freq.items()
            if len(neighbors) == freq
        )


# Problem 2685
# Link: https://leetcode.com/problems/count-the-number-of-complete-components/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        (6, [[0, 1], [0, 2], [1, 2], [3, 4]], 3),
        (6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]], 1),
    ]
    for n, edges, expected in cases:
        assert s.countCompleteComponents(n, edges) == expected
