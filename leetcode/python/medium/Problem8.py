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
    print(s.myAtoi("4.2"))
    print(s.myAtoi("   -042"))
    print(s.myAtoi("words and 987"))
    print(s.myAtoi("42"))
    print(s.myAtoi("1337c0d3"))
    print(s.myAtoi("0-1"))
    print(s.myAtoi("2147483648"))
    print(s.myAtoi("-2147483649"))
    print(s.myAtoi("31474836488"))
    print(s.myAtoi("   +0 123"))
