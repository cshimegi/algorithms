# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        stack = []
        if (numerator < 0) ^ (denominator < 0):
            stack.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        # Add integer part
        stack.append(str(numerator // denominator))

        # Check if remainder is 0
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(stack)

        # Add decimal point
        stack.append(".")
        remainder_history = {}
        while remainder != 0:
            if remainder in remainder_history:
                # If it's recurring decimal, we need to know where to place open bracket;
                # otherwise, we don't do it. For example, 0.5 doesn't need ()
                start_pos = remainder_history[remainder]
                stack.insert(start_pos, "(")
                stack.append(")")
                break

            remainder_history[remainder] = len(stack)
            remainder *= 10
            digit = remainder // denominator
            stack.append(str(digit))
            remainder %= denominator

        return "".join(stack)

# Problem 166
# Link: https://leetcode.com/problems/fraction-to-recurring-decimal/description/
# Tips:
if __name__ == '__main__':
    s = Solution()


