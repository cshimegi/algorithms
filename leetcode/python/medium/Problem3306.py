# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # O(n)/O(1)
        from collections import defaultdict

        vowels = "aeiou"
        vowel_counter = defaultdict(int)
        consonant_cnt = 0
        left = 0
        ans = 0
        valid_substring_count = 0  # Tracks valid substrings ending at `right`

        for right in range(len(word)):
            # Expand window
            if word[right] in vowels:
                vowel_counter[word[right]] += 1
            else:
                consonant_cnt += 1
                valid_substring_count = 0  # Reset count if consonant is added

            # Shrink window if too many consonants
            while consonant_cnt > k:
                if word[left] in vowels:
                    vowel_counter[word[left]] -= 1
                    if vowel_counter[word[left]] == 0:
                        del vowel_counter[word[left]]
                else:
                    consonant_cnt -= 1
                left += 1

            # Count valid substrings
            while consonant_cnt == k and len(vowel_counter) == 5:
                valid_substring_count += 1  # Count substrings
                if word[left] in vowels:
                    vowel_counter[word[left]] -= 1
                    if vowel_counter[word[left]] == 0:
                        del vowel_counter[word[left]]
                else:
                    consonant_cnt -= 1
                left += 1  # Move left pointer

            ans += valid_substring_count

        return ans

    def countOfSubstrings2(self, word: str, k: int) -> int:
        # Reference: https://www.youtube.com/watch?v=2wANakxRZNo
        from collections import defaultdict
        vowels = "aeiou"

        def atLeastK(k: int):
            vowel = defaultdict(int)
            l = len(word)
            consonant_cnt = 0
            left, ans = 0, 0
            for right in range(l):
                if word[right] in vowels:
                    vowel[word[right]] += 1
                else:
                    consonant_cnt += 1

                while len(vowel) == 5 and consonant_cnt >= k:
                    ans += (len(word) - right)
                    if word[left] in vowels:
                        vowel[word[left]] -= 1
                    else:
                        consonant_cnt -= 1

                    if vowel[word[left]] == 0:
                        del vowel[word[left]]
                    left += 1
            return ans

        return atLeastK(k) - atLeastK(k+1)


# Problem 3208
# Link: https://leetcode.com/problems/alternating-groups-ii/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ("aeioqq", 1, 0),
        ("aeiou", 0, 1),
        ("aeiou", 0, 1),
        ("ieaouqqieaouqq", 1, 3),
        ("ieplfcaoduqqiewaouqq", 2, 2),
        ("iqeaouqi", 2, 3),
    ]
    for words, k, expected in cases:
        assert s.countOfSubstrings(words, k) == expected
