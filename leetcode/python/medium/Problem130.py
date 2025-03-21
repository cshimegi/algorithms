# Questions to ask:
# 1. What is the time complexity? O(m*n)
# 2. What is the space complexity? O(m*n)
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m, n = len(board), len(board[0])

        def dfs(i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = "#"
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(i+di, j+dj)


        # Mark all 'O' in a region connected to edge
        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n-1] == "O":
                dfs(i, n-1)

        for j in range(n):
            if board[0][j] == "O":
                dfs(0, j)
            if board[m-1][j] == "O":
                dfs(m-1, j)

        # Flip all remaining `O`s to `X`, and convert `#` back to `O`
        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

# Problem 130
# Link: https://leetcode.com/problems/surrounded-regions/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    cases = [
        (
            [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]],
            [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
        ),
        ([["X"]], [["X"]])
    ]
    for board, expected in cases:
        s.solve(board)
        assert board == expected
