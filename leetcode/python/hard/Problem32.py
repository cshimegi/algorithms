# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize with -1 to track valid substring start
        max_count = 0

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)  # Store index of '('
            else:
                stack.pop()  # Pop last '(' index
                if not stack:
                    stack.append(i)  # Mark last invalid ')'
                else:
                    max_count = max(max_count, i - stack[-1])  # Compute valid length

        return max_count


# Problem 32
# Link: https://leetcode.com/problems/longest-valid-parentheses/description/
if __name__ == '__main__':
    s = Solution()

