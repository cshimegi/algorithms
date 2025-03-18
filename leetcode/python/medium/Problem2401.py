# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n, ans = len(nums), 1
        left, used_bits = 0, 0
        for right in range(n):
            # Shrink window and remove nums[left] from used_bits
            while used_bits & nums[right]:
                used_bits ^= nums[left]
                left += 1
            # add nums[right] to used_bits since any 2 elements in subarray won't have the same bits
            used_bits |= nums[right]

            ans = max(ans, right - left + 1)
        return ans

# Problem 2401
# Link: https://leetcode.com/problems/longest-nice-subarray/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1, 3, 8, 48, 10], 3),
        ([3, 1, 5, 11, 13], 1),
        ([1, 1, 1, 3, 8, 4, 48, 10, 1, 3, 8, 48, 10, 7], 4),
    ]
    for nums, expected in cases:
        assert s.longestNiceSubarray(nums) == expected
