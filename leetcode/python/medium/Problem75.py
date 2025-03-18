# Questions to ask:
# 1. What is the time complexity? O(n*log(n))
# 2. What is the space complexity? O(1)
# 3. Requirements:
#   - You must solve this problem without using the library's sort function.
from typing import List

class Solution:
    def partition(self, nums: List[int], low: int, high: int) -> int:
        # Choose pivot
        pivot = nums[high]
        i = low

        for j in range(low, high):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[high] = nums[high], nums[i]
        return i

    def quickSort(self, nums: List[int], low: int, high: int) -> None:
        if low < high:
            pivot = self.partition(nums, low, high)
            # Sort left side pivot
            self.quickSort(nums, low, pivot-1)
            # Sort right side of pivot
            self.quickSort(nums, pivot+1, high)

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quickSort(nums, 0, len(nums)-1)


# Problem 75
# Link: https://leetcode.com/problems/sort-colors/description/
# Reference: https://en.wikipedia.org/wiki/Dutch_national_flag_problem
# Counting sort can outperform here due to small number of distinct numbers in an array
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2])
    ]

    for nums, expected in cases:
        s.sortColors(nums)
        assert nums == expected
