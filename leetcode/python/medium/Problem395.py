# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
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

                right += 1

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
                    max_length = max(max_length, right - left)

        return max_length


    def longestSubstring2(self, s: str, k: int) -> int:
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
                return max(self.longestSubstring(sub, k) for sub in substrings)

        # If every character appears at least k times, return the length of the string
        return len(s)


# Problem 395
# Link: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    print(s.longestSubstring("abababacab", 5))
    print(s.longestSubstring("aaaaaabbbb", 5))
    print(s.longestSubstring("ababbc", 2))
