# Questions to ask:
# 1. What is the time complexity? O(log(n))
# 2. What is the space complexity? O(1)
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]

# Problem 153
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([3,4,5,1,2], 1),
        ([4,5,6,7,0,1,2], 0),
        ([11,13,15,17], 11)
    ]
    for nums, expected in cases:
        assert s.findMin(nums) == expected
