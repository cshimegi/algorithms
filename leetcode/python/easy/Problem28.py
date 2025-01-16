# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j, l, lh = 0, 0, len(needle), len(haystack)
        while j < lh:
            while j+i < lh and i < l and haystack[j+i] == needle[i]:
                i += 1

            if i == l:
                return j
            else:
                i = 0
            j += 1
        return -1


# Problem 28
# Tips:
# 1. Be careful of the cases which needle is longer than haystack
# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
if __name__ == '__main__':
    s = Solution()
    print(s.strStr(haystack = "sadbutsad", needle = "sad"))
    print(s.strStr(haystack = "leetcode", needle = "leeto"))
    print(s.strStr(haystack = "aaa", needle = "aaaa"))
    print(s.strStr(haystack = "mississippi", needle = "issip"))
    print(s.strStr(haystack = "misssp", needle = "ssp"))