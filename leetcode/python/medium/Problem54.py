# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []

        # Define the boundaries of the matrix
        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while top <= bottom and left <= right:
            # Traverse from left to right
            for j in range(left, right + 1):
                ans.append(matrix[top][j])
            top += 1  # Move the top boundary down

            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1  # Move the right boundary left

            if top <= bottom:
                # Traverse from right to left
                for j in range(right, left - 1, -1):
                    ans.append(matrix[bottom][j])
                bottom -= 1  # Move the bottom boundary up

            if left <= right:
                # Traverse from bottom to top
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1  # Move the left boundary right

        return ans



# Problem 54
# Link: https://leetcode.com/problems/spiral-matrix/description/
if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
