# Questions to ask:
# 1. What is the time complexity? O(n*log(n)) when m = n
# 2. What is the space complexity? O(n)
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Separate logs into letter logs and digit logs
        letter_logs = []
        digit_logs = []

        for log in logs:
            identifier, content = log.split(" ", maxsplit=1)
            if content[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((content, identifier))  # Store content first for sorting

        # Sort letter logs by (content, identifier) O(m*log(m))
        letter_logs.sort()

        # Reconstruct logs
        return [f"{identifier} {cont}" for cont, identifier in letter_logs] + digit_logs


# Problem 937
# Link: https://leetcode.com/problems/reorder-data-in-log-files/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        (
            ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"],
            ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"],
        ),
        (
            ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"],
            ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"],
        )
    ]

    for logs, expected in cases:
        assert s.reorderLogFiles(logs) == expected