# Questions to ask:
# 1. What is the time complexity? O(max(m, n)), where m and n are lengths of string1 and string2
# 2. What is the space complexity? O(m+n)
class Solution:
    def merge2Strings(self, string1: str, string2: str) -> str:
        from collections import Counter

        char_cnt_str1 = Counter(string1)
        char_cnt_str2 = Counter(string2)

        i1, i2 = 0, 0
        l1, l2 = len(string1), len(string2)

        ans = ""
        while i1 < l1 and i2 < l2:
            char1, char2 = string1[i1], string2[i2]
            # Compare occurrences of both characters.
            # If they are the same, add the lexicographically smaller one first.
            if char_cnt_str1[char1] == char_cnt_str2[char2]:
                if char1 <= char2:
                    ans += char1
                    i1 += 1
                else:
                    ans += char2
                    i2 += 1
            elif char_cnt_str1[char1] < char_cnt_str2[char2]:
                # If char1 occurrence is smaller than char2, add lesser one first
                ans += char1
                i1 += 1
            else:
                ans += char2
                i2 += 1

        # Add the remaining characters in one of the strings
        if i1 < l1:
            ans += string1[i1:]
        if i2 < l2:
            ans += string2[i2:]

        return ans

# Problem XXX2
# Link: from Ken (Agoda)
if __name__ == '__main__':
    s = Solution()
    cases = [
        ("dce", "cccbd", "dcecccbd"),
        ("super", "tower", "stouperwer")
    ]
    for string1, string2, expected in cases:
        print(s.merge2Strings(string1, string2) == expected)
