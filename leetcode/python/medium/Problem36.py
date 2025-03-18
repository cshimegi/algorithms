# Questions to ask:
# 1. What is the time complexity? O(1) because only 81 cells
# 2. What is the space complexity? O(1) because only 81 cells
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = [{str(i+1): False for i in range(9)} for _ in range(9)]
        rows = [{str(i+1): False for i in range(9)} for _ in range(9)]
        boxes = [{str(i+1): False for i in range(9)} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                box = (i // 3) * 3 + j // 3
                if cols[j][num] or rows[i][num] or boxes[box][num]:
                    return False
                cols[j][num] = True
                rows[i][num] = True
                boxes[box][num] = True
        return True


# Problem 36
# Link: https://leetcode.com/problems/valid-sudoku/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        (
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]
            ],
            True
        )
    ]
    for board, expected in cases:
        assert s.isValidSudoku(board) == expected
