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

    def lengthOfLongestSubstring2(self, s: str) -> int:
        len_s = len(s)
        if len_s == 0:
            return 0

        visited = {}
        start = 0
        ans = 0
        for i in range(len_s):
            if s[i] in visited:
                start = visited[s[i]]+1

            visited[s[i]] = i
            ans = max(ans, i-start+1)
        return ans

# Problem 3
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("tmmzuxt", 5),
        (" ", 1),
        ("ckilbkd", 5),
        ("$# $", 2),
    ]

    for string, expected in cases:
        assert s.lengthOfLongestSubstring(string) == expected
