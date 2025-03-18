# Questions to ask:
# 1. What is the time complexity? O(log n)
# 2. What is the space complexity? O(1)
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (r+l)//2
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


# Problem 33
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([4,5,6,7,0,1,2], 0, 4),
        ([4,5,6,7,0,1,2], 3, -1)
    ]
    for nums, target, expected in cases:
        assert s.search(nums, target) == expected
