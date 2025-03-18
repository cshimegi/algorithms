# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # Time: O(n) / Space: O(1)
        max_length = 0
        unique_chars = len(set(s))  # Maximum distinct chars

        # Try all possible numbers of unique characters
        for target_unique in range(1, unique_chars + 1):
            left, right = 0, 0
            char_count = {}
            unique, at_least_k = 0, 0  # Track unique chars and chars meeting k requirement

            while right < len(s):
                # Expand window by adding s[right]
                if s[right] in char_count:
                    char_count[s[right]] += 1
                else:
                    char_count[s[right]] = 1
                    unique += 1

                if char_count[s[right]] == k:
                    at_least_k += 1

                # Shrink window when unique characters exceed target
                while unique > target_unique:
                    if char_count[s[left]] == k:
                        at_least_k -= 1
                    char_count[s[left]] -= 1
                    if char_count[s[left]] == 0:
                        unique -= 1
                        del char_count[s[left]]
                    left += 1

                # If all unique chars meet the k condition, update max_length
                if unique == at_least_k:
                    max_length = max(max_length, right - left + 1)

                right += 1

        return max_length

    def longestSubstring2(self, s: str, k: int) -> int:
        # Time: O(n*log(n)) / Space: O(log(n))
        if not s:
            return 0

        # Count frequency of each character
        freq = {char: s.count(char) for char in set(s)}

        # Find any character that appears less than k times
        for char, count in freq.items():
            if count < k:
                # Split the string by this character
                substrings = s.split(char)
                # Recursively find the longest valid substring
                return max(self.longestSubstring2(sub, k) for sub in substrings)

        # If every character appears at least k times, return the length of the string
        return len(s)


# Problem 395
# Link: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    cases = [
        ("abababacab", 5, 0),
        ("aaaaaabbbb", 5, 6),
        ("ababbc", 2, 5),
    ]
    for string, k, expected in cases:
        assert s.longestSubstring(string, k) == expected
        assert s.longestSubstring2(string, k) == expected
