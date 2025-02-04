# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        # Step 1: Build adjacency list (pattern-based)
        neighbors = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbors[pattern].append(word)

        # Step 2: BFS Initialization
        queue = deque([(beginWord, 1)])  # (word, transformation_steps)
        visited = set([beginWord])

        # Step 3: BFS Traversal
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps  # Found shortest path

            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                for neighbor in neighbors[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))

        return 0


# Problem 127
# Link: https://leetcode.com/problems/word-ladder/description/
if __name__ == '__main__':
    s = Solution()
