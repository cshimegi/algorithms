# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_NUM = -2147483648
        MAX_NUM = 2147483647

        negative = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = dividend // divisor
        return min(MAX_NUM, max(MIN_NUM, quotient if not negative else -quotient))


    def divide2(self, dividend: int, divisor: int) -> int:
        MIN_NUM = -2147483648
        MAX_NUM = 2147483647

        quotient = 0
        negative = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            temp = divisor
            multiply = 1
            # Find the largest multiply by shifting for better performance
            while dividend >= (temp << 1):
                temp <<= 1
                multiply <<= 1
            dividend -= temp
            quotient += multiply

        return min(MAX_NUM, max(MIN_NUM, quotient if not negative else -quotient))

# Problem 22
# Link: https://leetcode.com/problems/divide-two-integers/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        (10, 3, 3),
        (7, -3, -2),
    ]
    for dividend, divisor, expected in cases:
        assert s.divide(dividend, divisor) == expected
        assert s.divide2(dividend, divisor) == expected
