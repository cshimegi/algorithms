# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
# Refer to 63
class Solution:
    def backtrack(self, m: int, n: int, right_cnt: int = 0, down_cnt: int = 0):
        # Time Limit Exceeded

        # -1 because positions of robot and goal are not counted in path
        if m-1 == right_cnt and n-1 == down_cnt:
            return 1

        ans = 0
        if right_cnt < m:
            ans += self.backtrack(m, n, right_cnt + 1, down_cnt)

        if down_cnt < n:
            ans += self.backtrack(m, n, right_cnt, down_cnt + 1)

        return ans

    def uniquePaths(self, m: int, n: int) -> int:
        # O(m*n) Time | O(m*n) Space
        # Initialize a 2D DP array
        dp = [[1] * n for _ in range(m)]

        # Fill the DP table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] # top + left

        return dp[m - 1][n - 1]

    def uniquePaths2(self, m: int, n: int) -> int:
        # O(m*n) Time | O(n) Space, Optimize Space complexity
        # Initialize a 1D DP array
        dp = [1] * n

        # Update the DP array for each row
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1] # from top and left
        return dp[-1]


# Problem 62
# Link: https://leetcode.com/problems/unique-paths/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        (10, 3, 55)
    ]

    for m, n, expected in cases:
        assert s.uniquePaths(m, n) == expected
        assert s.uniquePaths2(m, n) == expected
