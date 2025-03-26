# Questions to ask:
# 1. What is the time complexity? O(m*n*log(m*n))
# 2. What is the space complexity? O(m*n)
class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        flatten_grid = [num for row in grid for num in row]
        flatten_grid.sort()

        total = len(flatten_grid)
        # total // 2 or (total - 1) // 2 can work
        mid_num = flatten_grid[total // 2]

        ans = 0
        for num in flatten_grid:
            if num % x != mid_num % x:
                return -1
            ans += abs(mid_num - num) // x

        return ans


# Problem 2033
# Link: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/editorial/description/
# Ref: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/editorial/?envType=daily-question&envId=2025-03-26
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([[2, 4], [6, 8]], 2, 4),
        ([[1, 5], [2, 3]], 1, 5),
        ([[1, 2], [3, 4]], 2, -1),
    ]
    for grid, x, expected in cases:
        assert s.minOperations(grid, x) == expected
