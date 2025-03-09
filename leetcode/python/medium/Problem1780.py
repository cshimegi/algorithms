# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True


# Problem 1780
# Link: https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        12,
        21,
        91
    ]
    for case in cases:
        print(s.checkPowersOfThree(case))
