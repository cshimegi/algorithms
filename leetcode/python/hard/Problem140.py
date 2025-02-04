# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        wordSet = set(wordDict)  # Convert list to set for O(1) lookup

        def backtrack(start: int) -> list[str]:
            if start == len(s):
                return [""]  # Base case: return empty sentence

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    for sub in backtrack(end):  # Explore further splits
                        sentences.append(word + (" " + sub if sub else ""))

            return sentences

        return backtrack(0)


# Problem 140
# Link: https://leetcode.com/problems/word-break-ii/description/
if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))
