# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1 > 0:
                count += 1
            n = n >> 1
        return count

    def hammingWeight2(self, n: int) -> int:
        return bin(n).count('1')

# Problem 191
# Tips:
# 1. 
# Link: https://leetcode.com/problems/number-of-1-bits/description/
if __name__ == '__main__':
    s = Solution()

