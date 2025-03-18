# Questions to ask:
# 1. What is the time complexity? O(m*n)
# 2. What is the space complexity? O(m*n)
class Solution:
    """ DP table of first sample
    # ''  r  o  s
   ''  0  1  2  3
    h  1  1  2  3
    o  2  2  1  2
    r  3  2  2  2
    s  4  3  3  2
    e  5  4  4  3
    """
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # Update edit distance to form word1
        for i in range(m + 1):
            dp[i][0] = i
        # Update edit distance to form word2
        for j in range(n + 1):
            dp[0][j] = j
        # Update edit distance to transform word1 to word2
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]: # no need to change if current chars are the same
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[m][n]

# Problem 72
# Link: https://leetcode.com/problems/edit-distance/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ("horse", "ros", 3),
        ("intention", "execution", 5),
    ]
    for word1, word2, expected in cases:
        assert s.minDistance(word1, word2) == expected
