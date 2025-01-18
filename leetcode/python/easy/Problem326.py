# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
# 3. Requirements:
#   - Could you solve it without loops/recursion?
#    2^31 - 1 = 3^x => x ~= 19.55
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3**19 % n == 0


# Problem 326
# Tips:
# Link: https://leetcode.com/problems/power-of-three/description/
if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfThree(27))
    print(s.isPowerOfThree(0))
    print(s.isPowerOfThree(9))
    print(s.isPowerOfThree(45))
    print(s.isPowerOfThree(8))
