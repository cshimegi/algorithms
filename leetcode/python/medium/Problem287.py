# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(1)
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd’s Tortoise and Hare Algorithm (Cycle Detection)
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]      # Move slow by 1 step
            fast = nums[nums[fast]]  # Move fast by 2 steps

        # Step 2: Find the cycle start (duplicate number)
        slow = 0  # Reset slow to start
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

# Problem 287
# Link: https://leetcode.com/problems/find-the-duplicate-number/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1,3,4,2,2], 2),
        ([3,1,3,4,2], 3)
    ]
    for nums, expected in cases:
        assert s.findDuplicate(nums) == expected
