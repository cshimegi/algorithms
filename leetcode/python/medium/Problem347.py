# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # 32-bit mask (4294967295 in decimal)
        INT_MAX = 0x7FFFFFFF  # Max positive int in 32-bit

        while b != 0:
            # XOR computes sum without carry
            sum_without_carry = (a ^ b) & MASK

            # AND computes carry, shift left to add carry
            carry = ((a & b) << 1) & MASK

            # Update values for next iteration
            a, b = sum_without_carry, carry

        # Handle negative results (convert back to signed 32-bit integer)
        return a if a <= INT_MAX else ~(a ^ MASK)


# Problem 371
# Link: https://leetcode.com/problems/sum-of-two-integers/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    print(s.getSum(4,19))
    print(s.getSum(2,3))
    print(s.getSum(-3, 20))
    print(s.getSum(-10,-9))

