# Questions to ask:
# 1. What is the time complexity?
# Trie Construction: 𝑂(𝑊𝐿)
# DFS: O(m⋅n⋅4^L)
# 2. What is the space complexity?
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store complete words at the end nodes

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word  # Mark the end of the word

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m, n = len(board), len(board[0])
        # Build Trie from words
        trie = Trie()
        for word in words:
            trie.insert(word)

        ans = set()

        def dfs(i, j, node):
            char = board[i][j]
            if char not in node.children:
                return

            next_node = node.children[char]
            if next_node.word:
                ans.add(next_node.word)  # Found a valid word

            # Mark as visited by modifying board
            board[i][j] = "#"

            # Explore all 4 directions
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] in next_node.children:
                    dfs(ni, nj, next_node)

            # Restore board state (Backtracking)
            board[i][j] = char

            # Optimization: Remove leaf nodes in Trie
            if not next_node.children:
                del node.children[char]

        # Start DFS from every cell
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root.children:
                    dfs(i, j, trie.root)

        return list(ans)


# Problem 212
# Link: https://leetcode.com/problems/word-search-ii/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        [
            [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
            ["oath","pea","eat","rain"]
        ],
        [
            [["a","b"],["c","d"]],
            ["abcb"]
        ]
    ]
    for board, words in cases:
        print(s.recoverFromPreorder(board, words))

