# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(1)
class Solution:
    def myAtoi(self, s: str) -> int:
        MIN_INT, MAX_INT = -2**31, 2**31-1

        ans = 0
        first_char = None
        is_negative = False
        for c in s:
            # Ignore leading spaces
            if first_char is None and c == " ":
                continue

            if first_char is None:
                first_char = c
                if first_char == "-" or first_char == "+":
                    is_negative = first_char == "-"
                elif first_char.isdigit():
                    ans = ans * 10 + int(first_char)
                else:
                    break
            else:
                if c.isdigit():
                    ans = ans * 10 + int(c)
                else:
                    break

        if is_negative:
            ans = max(-ans, MIN_INT)
        else:
            ans = min(ans, MAX_INT)

        return ans


# Problem 8
# Link: https://leetcode.com/problems/string-to-integer-atoi/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ("4.2", 4),
        ("   -042", -42),
        ("words and 987", 0),
        ("42", 42),
        ("1337c0d3", 1337),
        ("0-1", 0),
        ("2147483648", 2147483647),
        ("-2147483649", -2147483648),
        ("31474836488", 2147483647),
        ("   +0 123", 0)
    ]
    for string, expected in cases:
        assert s.myAtoi(string) == expected
