# Questions to ask:
# 1. What is the time complexity? O(W * 4^L)
# 2. What is the space complexity? O(m * n)
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, lw = len(board), len(board[0]), len(word)

        # Check if the word is possible given the board
        from collections import Counter
        board_counter = Counter(char for row in board for char in row)
        word_counter = Counter(word)
        for char, count in word_counter.items():
            if board_counter[char] < count:
                return False

        def dfs(i: int, j: int, k: int) -> bool:
            # Base case: if the entire word is matched
            if k == lw:
                return True

            # Out-of-bounds or mismatch
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False

            # Mark the current cell as visited
            temp = board[i][j]
            board[i][j] = '#'

            # Explore neighbors (up, down, left, right)
            for x, y in [(0,1), (0,-1), (1,0), (-1,0)]:
                if dfs(i+x, j+y, k+1):
                    return True

            # Restore the cell after backtracking
            board[i][j] = temp
            return False

        # Start DFS from every cell
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):  # Start matching from word[0]
                    return True

        return False

# Problem 79
# Link: https://leetcode.com/problems/word-search/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
    ]
    for board, word, expected in cases:
        assert s.exist(board, word) == expected
