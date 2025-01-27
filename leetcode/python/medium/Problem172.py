# Questions to ask:
# 1. What is the time complexity? O(log n)
# 2. What is the space complexity?
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


