# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(n)
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n-2):
            if nums[i] == 0:
                for j in range(i, i+3):
                    nums[j] ^= 1
                ans += 1

        return ans if sum(nums) == n else -1

    def minOperations2(self, nums: List[int]) -> int:
        n = len(nums)
        prev1, prev2 = 0, 0
        ans = 0
        for i in range(n-2):
            if nums[i] ^ prev1 ^ prev2:
                prev2 = prev1
                prev1 = 0
            else:
                ans += 1
                prev2 = prev1
                prev1 = 1
        return ans if nums[n-1] ^ prev1 and nums[n-2] ^ prev1 ^ prev2 else -1

# Problem 3191
# Link: https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([0,1,1,1,0,0], 3),
        ([0,1,1,1], -1),
    ]
    for nums, expected in cases:
        assert s.minOperations(nums) == expected
        assert s.minOperations2(nums) == expected
