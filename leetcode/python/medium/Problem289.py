# Questions to ask:
# 1. What is the time complexity? O(m*n)
# 2. What is the space complexity? O(1)
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check(r: int, c: int):
            count1 = 0
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]:
                if 0 <= r+dr < row and 0 <= c+dc < col:
                    if board[r+dr][c+dc] == 1 or board[r+dr][c+dc] == -1:
                        count1 += 1

            if board[r][c] == 1:
                if 2 > count1 or 3 < count1:
                    # -1 is for next dead state of current live cell
                    board[r][c] = -1
            else:
                if count1 == 3:
                    # 2 is for next live state of current dead cell
                    board[r][c] = 2

        # Check and mark the cells which need to be changed
        row, col = len(board), len(board[0])
        for r in range(row):
            for c in range(col):
                check(r, c)

        # Change the marked cells
        for r in range(row):
            for c in range(col):
                if board[r][c] == -1:
                    board[r][c] = 0
                elif board[r][c] == 2:
                    board[r][c] = 1

# Problem 289
# Link: https://leetcode.com/problems/game-of-life/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    cases = [
        [[0,1,0],[0,0,1],[1,1,1],[0,0,0]],
    ]
    for board in cases:
        s.gameOfLife(board)
        print(board)
