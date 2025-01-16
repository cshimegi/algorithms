# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def mySqrt(self, x: int) -> int:
        # Newton's method
        fx = x        # The input number `x` whose square root is to be found.
        px = 0        # Previous approximation (initialized to 0).
        cx = 1        # Current approximation (start with a guess of 1).

        while abs(cx-px) >= 1:
            cx, px = (cx+fx/cx)/2, cx

        return int(cx)

# Problem 69
# Tips:
# 1.
# Link: https://leetcode.com/problems/sqrtx/description/
if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(x = 4))
