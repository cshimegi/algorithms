# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(min(n,m)) where m is the size of the character set.
# 3. Requirements:
#   - Substring is without repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        i = 0
        v = {}

        for j, char in enumerate(s):
            if char in v and v[char] >= i:
                # Move to one past the last occurrence
                i = v[char] + 1
            # Update the last seen index of the character
            v[char] = j
            ans = max(ans, j - i + 1)

        return ans

# Problem 3
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring(s = "abcabcbb"))
    print(s.lengthOfLongestSubstring(s = "bbbbb"))
    print(s.lengthOfLongestSubstring(s = "pwwkew"))
    print(s.lengthOfLongestSubstring(s = "tmmzuxt"))
    print(s.lengthOfLongestSubstring(s = " "))
    print(s.lengthOfLongestSubstring(s = "ckilbkd"))
    print(s.lengthOfLongestSubstring(s = "$# $"))
