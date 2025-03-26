# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [0] * n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        # Connect x to y
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Build component
        uf = UnionFind(n)
        for u, v, w in edges:
            uf.union(u, v)

        # Get cost of each component
        component_cost = {}
        for u, v, w in edges:
            root = uf.find(u)
            if root not in component_cost:
                component_cost[root] = w
            else:
                component_cost[root] &= w

        # Queries
        ans = []
        for u, v in query:
            root_u = uf.find(u)
            root_v = uf.find(v)
            if root_u == root_v:
                ans.append(component_cost[root_u])
            else:
                ans.append(-1)
        return ans


# Problem 3108
# Link: https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        (5, [[0,1,7],[1,3,7],[1,2,1]], [[0,3],[3,4]], [1, -1]),
        (3, [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], [[1,2]], [0]),
    ]
    for n, edges, query, expected in cases:
        assert s.minimumCost(n, edges, query) == expected
