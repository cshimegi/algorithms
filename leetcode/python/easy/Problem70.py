# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def climbStairs(self, n: int) -> int:
        x1, x2 = 1, 2

        if n == 1:
            return x1
        if n == 2:
            return x2

        for i in range(3, n+1):
            x1, x2 = x2, x1 + x2
        return x2


# Problem 70
# Tips:
# 1.
# Link: https://leetcode.com/problems/climbing-stairs/description/
if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3))
