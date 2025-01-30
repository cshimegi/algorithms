# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def dfs(i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] == '#':
                return False

            if matrix[i][j] == target:
                return True

            matrix[i][j] = '#'

            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                if dfs(i+di, j+dj):
                    return True

            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j):
                    return True
        return False

    def searchMatrix2(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1  # Start from the top-right corner

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1  # Move left
            else:
                row += 1  # Move down

        return False

# Problem 240
# Link: https://leetcode.com/problems/search-a-2d-matrix-ii/description/
# Tips:
if __name__ == '__main__':
    s = Solution()

