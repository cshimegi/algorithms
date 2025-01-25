# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        l = len(s)
        dp = [0] * (l + 1)

        dp[0] = 1  # 2-character
        dp[1] = 1  # Single character, if not '0'
        for i in range(2, l + 1):
            # Check single-character decoding
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]

            # Check two-character decoding
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[l]


# Problem 91
# Link: https://leetcode.com/problems/decode-ways/description/
# Tips:
# - Since we can take either single character or two characters, we can consider it a problem like
#   how many valid ways it can take 1 step or 2 steps to walk from point A to point B on a straight line
if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("123522"))
