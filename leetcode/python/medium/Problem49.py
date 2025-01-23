# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = {}
        for s in strs:
            key = ''.join(sorted(s))
            ans[key] = ans.get(key, []) + [s]
        return [v for v in ans.values()]


# Problem 49
# Link: https://leetcode.com/problems/group-anagrams/description/
if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
