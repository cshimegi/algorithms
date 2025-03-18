# Questions to ask:
# 1. What is the time complexity? O(m*n)
# 2. What is the space complexity? O(1)
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Calculate the sum of first column
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        # Calculate the sum of first row
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        # Calculate the minimum sum of other cells
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]


# Problem 64
# Link: https://leetcode.com/problems/minimum-path-sum/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
        ([[1, 2, 3], [4, 5, 6]], 12)
    ]
    for grid, expected in cases:
        assert s.minPathSum(grid) == expected