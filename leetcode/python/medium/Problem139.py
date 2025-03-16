# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def dfs(self, s: str, memo: dict, wordMap: dict) -> bool:
        if s in memo:
            return memo[s]
        elif s in wordMap:
            return True

        for i in range(1, len(s)):
            if s[:i] in wordMap and self.dfs(s[i:], memo, wordMap):
                memo[s] = True
                return True

        memo[s] = False
        return False

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # DFS Time:O(n^2)/Space:O(n)
        wordMap = {w: 1 for w in wordDict}
        memo = {}
        return self.dfs(s, memo, wordMap)

    def wordBreak2(self, s: str, wordDict: list[str]) -> bool:
        # DP Time:O(n)/Space:O(n)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True # empty string can always be segmented
        max_len = max(map(len, wordDict))

        for i in range(1, n+1):
            # Backward
            for j in range(i-1, max(i-max_len-1, -1), -1): # consider only the length of word <= max_len
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True # Mark the position of last character of found word true
                    break
        return dp[n]


# Problem 139
# Link: https://leetcode.com/problems/word-break/description/
# Tips:
if __name__ == '__main__':
    s = Solution()

