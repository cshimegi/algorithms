# Questions to ask:
# 1. What is the time complexity? O(log n)
# 2. What is the space complexity?
from typing import List

class Solution:
    def binarySearch(self, nums: List[int], target: int, find_lowest: bool) -> int:
        l, r, ans = 0, len(nums)-1, -1
        while  l <= r:
            mid = (r+l)//2
            if nums[mid] == target:
                if ans == -1:
                    ans = mid

                if find_lowest:
                    if mid < ans:
                        ans = mid
                    r = mid - 1
                else:
                    if mid > ans:
                        ans = mid
                    l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return ans


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.binarySearch(nums, target, True)
        r = self.binarySearch(nums, target, False)
        return [l, r]


# Problem 34
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([5,8,8,8,8,10], 8, [1,4]),
        ([5,7,7,8,8,10], 6, [-1,-1]),
        ([8,8,8,8,8,8], 8, [0,5])
    ]
    for nums, target, expected in cases:
        assert s.searchRange(nums, target) == expected
