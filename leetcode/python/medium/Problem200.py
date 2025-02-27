# Questions to ask:
# 1. What is the time complexity? O(m*n)
# 2. What is the space complexity? O(m*n)
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return

            grid[i][j] = "#"

            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(i+di, j+dj)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1
        return ans


# Problem 200
# Link: https://leetcode.com/problems/number-of-islands/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
