# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = {}
        for c in s:
            visited.update({c: visited.get(c, 0) + 1})
        for i in range(len(s)):
            if visited[s[i]] == 1:
                return i
        return -1

# Problem 387
# Tips:
# Link: https://leetcode.com/problems/first-unique-character-in-a-string/description/
if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar(s = "leetcode"))
    print(s.firstUniqChar(s = "loveleetcode"))

