# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
# Different from 62
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # O(m*n) Time | O(n) Space
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1] # From left and top

        return dp[-1]


    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        # O(m*n) Time | O(m*n) Space
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]  # From top
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]  # From left

        return dp[-1][-1]

# Problem 63
# Link: https://leetcode.com/problems/unique-paths-ii/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([[0,0,0],[0,1,0],[0,0,0]], 2),
        ([[0,1],[0,0]], 1),
        ([[0], [0]], 1),
        ([[1,0], [0,0]], 0),
        ([[0,0,0], [1,1,1], [0,0,0]], 0)
    ]
    for obstacleGrid, expected in cases:
        assert s.uniquePathsWithObstacles(obstacleGrid) == expected
        assert s.uniquePathsWithObstacles2(obstacleGrid) == expected