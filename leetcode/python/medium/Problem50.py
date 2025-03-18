# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_reciprocal = n < 0
        n = abs(n)
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans *= x
            x *= x
            n //= 2
        return ans if not is_reciprocal else 1 / ans

# Problem 50
# Link: https://leetcode.com/problems/powx-n/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        (2.0, 10, 1024.0),
        (2.0, -2, 0.25)
    ]
    for x, n, expected in cases:
        assert s.myPow(x, n) == expected
