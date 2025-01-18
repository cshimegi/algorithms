# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(1)
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total = (n * (n + 1)) // 2
        return total - sum(nums)

# Problem 268
# Tips:
# Link: https://leetcode.com/problems/missing-number/description/
if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber(nums = [3,0,1]))
