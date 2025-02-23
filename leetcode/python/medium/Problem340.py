class Solution:
    # Questions to ask:
    # 1. What is the time complexity? O(n)
    # 2. What is the space complexity?
    def longestSubstringWithKDistinctChars(self, string: str, k: int) -> int:
        from collections import Counter

        i, j = 0, 0
        max_len = 0
        char_count = Counter()
        while j < len(string):
            char_count[string[j]] += 1
            if len(char_count) > k:
                # Shrink window because we have more than k distinct chars
                char_count[string[i]] -= 1
                if char_count[string[i]] == 0:
                    del char_count[string[i]]
                i += 1
            else:
                max_len = max(max_len, j - i + 1)
            j += 1
        return max_len


# Problem 340
# Link: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
# https://memorylimitexceeded.gitlab.io/leetcode/problems/0340-longest-substring-with-at-most-k-distinct-characters.html
if __name__ == '__main__':
    s = Solution()
    cases = [
        ("ecebaa", 2), # 3
        ("aabacccac", 2), # 6
        ("aabacccac", 1), # 3
    ]
    for string, k in cases:
        print(s.longestSubstringWithKDistinctChars(string, k))

