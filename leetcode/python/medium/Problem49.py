# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # O(n * m * log(m))
        ans = {}
        for s in strs:
            key = ''.join(sorted(s))
            ans[key] = ans.get(key, []) + [s]
        return [v for v in ans.values()]

    def groupAnagrams2(strs: list[str]) -> list[list[str]]:
        # O(n * m)
        from collections import defaultdict

        ans = defaultdict(list)

        for s in strs:
            # Create a frequency tuple (hashable)
            char_count = [0] * 26  # 26 letters in lowercase English

            for char in s:
                char_count[ord(char) - ord('a')] += 1

            key = tuple(char_count)  # Convert to tuple (hashable)
            ans[key].append(s)

        return list(ans.values())


# Problem 49
# Link: https://leetcode.com/problems/group-anagrams/description/
if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
