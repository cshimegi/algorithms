# Questions to ask:
# 1. What is the time complexity? O(m+n)
# 2. What is the space complexity? O(1)
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1  # start from top right
        while 0 <= i < m and 0 <= j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1

        return False


# Problem 74
# Link: https://leetcode.com/problems/search-a-2d-matrix/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False)
    ]

    for matrix, target, expected in cases:
        assert s.searchMatrix(matrix, target) == expected
