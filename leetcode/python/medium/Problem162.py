# Questions to ask:
# 1. What is the time complexity? O(log n)
# 2. What is the space complexity? O(1)
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # O(log n)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left+right)//2
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid # peak is on the left half (including mid)
        return left

    def findPeakElement2(self, nums: List[int]) -> int:
        """
        To always return the index of first peak (from left to right of nums)
        :param nums:
        :return:
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # Always move left if nums[mid] is a peak or greater than nums[mid + 1]
            if nums[mid] > nums[mid + 1]:
                right = mid  # Move left, including the current peak candidate
            else:
                left = mid + 1  # Move right if the next element is greater

        return left

    def findPeakElement3(self, nums: List[int]) -> int:
        # O(n)
        l = len(nums)

        if l == 1:
            return 0

        for i in range(0, l):
            if 0 < i < l-1 and nums[i] > nums[i+1] and nums[i] > nums[i-1]:
                return i
            elif i == 0 and nums[i+1] < nums[i]:
                return i
            elif i == l-1 and nums[i-1] < nums[i]:
                return i

        return -1



# Problem 162
# Link: https://leetcode.com/problems/find-peak-element/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1,2,3,1], 2),
        ([1,2,1,3,5,6,4], 5),
        ([1,2,3,4,5,6,7,8,9], 8)
    ]
    for nums, expected in cases:
        assert s.findPeakElement(nums) == expected
