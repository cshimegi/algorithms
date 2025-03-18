# Questions to ask:
# 1. What is the time complexity? O(n^2)
# 2. What is the space complexity?
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Reverse each row
        for i in range(n//2):
            for j in range(n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-i][j]
                matrix[n-1-i][j] = temp

        # Transpose matrix
        for i in range(n):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp


# Problem 48
# Link: https://leetcode.com/problems/rotate-image/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        [[1,2,3],[4,5,6],[7,8,9]],
        [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    ]
    for matrix in cases:
        s.rotate(matrix)
        print(matrix)
