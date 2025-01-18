# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        if ls != lt:
            return False
        records = {}
        for i in range(ls):
            os, ot = ord(s[i]), ord(t[i])
            records.update({os: records.get(os, 0)+1})
            records.update({ot: records.get(ot, 0)-1})
        for v in records.values():
            if v != 0:
                return False
        return True

# Problem 234
# Tips:
# Link: https://leetcode.com/problems/palindrome-linked-list/description/
if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))
    print(s.isAnagram("rat", "car"))
