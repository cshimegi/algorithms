# Questions to ask:
# 1. What is the time complexity? O(n*log(max(nums) - min(nums)))
# 2. What is the space complexity? O(1)
from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        total = len(nums)

        def canStealK(capability: int) -> bool:
            i, count = 0, 0
            while i < total:
                if nums[i] <= capability:
                    count += 1
                    i += 2
                else:
                    i += 1

            return count >= k

        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if canStealK(mid): # guess capability
                right = mid # because we want min capability
            else:
                left = mid + 1

        return left


# Problem 2560
# Link: https://leetcode.com/problems/house-robber-iv/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([2, 3, 5, 9], 2, 5),
        ([2, 7, 9, 3, 1], 2, 2)
    ]
    for nums, k, expected in cases:
        assert s.minCapability(nums, k) == expected
