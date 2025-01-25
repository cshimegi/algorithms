# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows = [0]*m
        cols = [0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1

        for i in range(m):
            for j in range(n):
                if cols[j] == 1 or rows[i] == 1:
                    matrix[i][j] = 0

    def setZeroes2(self, matrix: list[list[int]]) -> None:
        """
        Optimized Space Complexity O(1)
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Mark zeros in the first row and first column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Use the markers to set rows and columns to zero
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Handle the first row and column separately
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


# Problem 73
# Link: https://leetcode.com/problems/set-matrix-zeroes/description/
if __name__ == '__main__':
    s = Solution()
    print(s.setZeroes([[1,2,3], [1,0,1], [2,3,0]]))
