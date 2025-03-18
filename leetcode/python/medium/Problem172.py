# Questions to ask:
# 1. What is the time complexity? O(log n)
# 2. What is the space complexity? O(1)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n > 0:
            n //= 5
            ans += n
        return ans

# Problem 172
# Link: https://leetcode.com/problems/factorial-trailing-zeroes/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    cases = [
        (3, 0),
        (5, 1),
        (0, 0),
    ]
    for n, expected in cases:
        assert s.trailingZeroes(n) == expected
