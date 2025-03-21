# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(n)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        from collections import defaultdict

        ans = 0
        counter = defaultdict(int)
        left, right, ls = 0, 0, len(s)
        validSubStringNum = 0
        while right < ls:
            counter[s[right]] += 1

            while len(counter) == 3:
                validSubStringNum += 1
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]

                left += 1
            ans += validSubStringNum
            right += 1

        return ans

# Problem 1358
# Link: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ("abcabc", 10),
        ("aaacb", 3),
        ("abc", 1),
    ]
    for string, expected in cases:
        assert s.numberOfSubstrings(string) == expected
