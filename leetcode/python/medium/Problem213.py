# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(1)
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(nums: List[int]) -> int:
            prev_rob, prev_skip = 0, 0
            for num in nums:
                curr = prev_skip + num
                prev_skip = max(prev_rob, prev_skip)
                prev_rob = curr
            return max(prev_rob, prev_skip)

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # max(exclude first, exclude last)
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))

# Problem 213
# Link: https://leetcode.com/problems/house-robber-ii/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([2, 3, 2], 3),
        ([1, 2, 3, 1], 4),
        ([1, 2, 3], 3),
    ]
    for nums, expected in cases:
        assert s.rob(nums) == expected
