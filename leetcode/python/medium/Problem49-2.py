# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity?
from typing import List

class Solution:
    def searchAllAnagrams(self, string: str, pattern: str) -> List[int]:
        from collections import Counter
        ans = []

        l_pattern = len(pattern)
        pattern_counter = Counter(pattern)
        window_counter = Counter(string[:l_pattern])
        if pattern_counter == window_counter:
            ans.append(0)

        for i in range(1, len(string) - l_pattern + 1):
            window_counter[string[i-1]] -= 1
            window_counter[string[i+l_pattern-1]] += 1
            if pattern_counter == window_counter:
                ans.append(i)

        return ans


# Problem 49-2
# Link:
if __name__ == '__main__':
    s = Solution()
    cases = [
        ("abcsdacncbaasedf", "abc", [0, 8]),
    ]

    for string, pattern, expected in cases:
        assert s.searchAllAnagrams(string, pattern) == expected
