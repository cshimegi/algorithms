# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)

        ans = 0
        while x > 0:
            ans = ans * 10 + x % 10
            x //= 10

        if is_negative and -ans < -2**31 or not is_negative and ans > 2**31-1:
            return 0

        return ans if not is_negative else ans * -1


# Problem 7
# Link: https://leetcode.com/problems/reverse-integer/description/
if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))