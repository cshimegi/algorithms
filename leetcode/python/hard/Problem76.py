# Questions to ask:
# 1. What is the time complexity? O(m + n)
# 2. What is the space complexity?
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if not s or not t:
            return ""

        target_count = Counter(t)  # Frequency of characters in t
        window_count = {}

        left, right = 0, 0
        min_len = float('inf')
        min_start = 0
        required_chars = len(target_count)  # Unique characters in t
        formed_chars = 0  # Number of chars that meet the requirement

        while right < len(s):
            # Expand window
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            if char in target_count and window_count[char] == target_count[char]:
                formed_chars += 1

            # Try to shrink the window from the left
            while left <= right and formed_chars == required_chars:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                # Remove leftmost character from window
                left_char = s[left]
                window_count[left_char] -= 1

                if left_char in target_count and window_count[left_char] < target_count[left_char]:
                    formed_chars -= 1

                left += 1  # Move left pointer

            right += 1  # Move right pointer

        return s[min_start:min_start + min_len] if min_len != float('inf') else ""


# Problem 76
# Link: https://leetcode.com/problems/minimum-window-substring/description/
if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("a", "a"))

