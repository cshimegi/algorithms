# Questions to ask:
# 1. What is the time complexity? O(n*2^n)
# 2. What is the space complexity? O(n*2^n)
from typing import List

class Solution:
    def isPalindrome(self, sub_str: str) -> bool:
        return sub_str == sub_str[::-1]

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        l = len(s)

        def backtrack(start: int, path: List[str]):
            # If we have reached the end of the string, add the current partition to the result
            if start == l:
                ans.append(path[:])
                return
            # Explore all possible substrings starting from `start`
            for end in range(start, l):
                if self.isPalindrome(s[start:end+1]):
                    # Choose: Add the current substring to the path
                    path.append(s[start:end+1])
                    # Explore further partitions
                    backtrack(end+1, path)
                    # Undo the choice
                    path.pop()

        backtrack(0, [])
        return ans


# Problem 131
# Link: https://leetcode.com/problems/palindrome-partitioning/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    cases = [
        ("a", [["a"]]),
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
    ]
    for string, expected in cases:
        assert s.partition(string) == expected
