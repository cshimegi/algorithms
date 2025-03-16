# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True

            if nums[l] == nums[mid] == nums[r]: # Eliminate duplicates from search space
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False


# Problem 81
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([2, 5, 6, 0, 0, 1, 2], 0),
        ([2, 5, 6, 0, 0, 1, 2], 3)
    ]
    for nums, target in cases:
        print(s.search(nums, target))
