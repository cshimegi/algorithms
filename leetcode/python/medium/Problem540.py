# Questions to ask:
# 1. What is the time complexity? O(log n)
# 2. What is the space complexity?
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            # Since every element appears exactly twice except for one,
            # the starting index of duplicate numbers must be even.
            # Ensure mid is even for proper pairing
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid

        return nums[l]


# Problem 540
# Link: https://leetcode.com/problems/single-element-in-a-sorted-array/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        [1,1,2,3,3,4,4,8,8],
        [3,3,7,7,10,11,11]
    ]

    for nums in cases:
        print(s.singleNonDuplicate(nums))

