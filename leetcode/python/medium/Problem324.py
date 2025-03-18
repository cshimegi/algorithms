# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(1)
from typing import List
from random import randint 

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quickselect(k: int):
            """ QuickSelect to find the k-th smallest element (Median). """
            left, right = 0, len(nums) - 1
            while left < right:
                pivot = partition(left, right)
                if pivot == k:
                    return nums[pivot]
                elif pivot < k:
                    left = pivot + 1
                else:
                    right = pivot - 1
            return nums[left]

        def partition(left: int, right: int):
            """ Lomuto partition scheme for QuickSelect. """
            pivot_idx = randint(left, right)
            pivot_val = nums[pivot_idx]
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]  # Move pivot to end
            store_idx = left
            for i in range(left, right):
                if nums[i] < pivot_val:
                    nums[i], nums[store_idx] = nums[store_idx], nums[i]
                    store_idx += 1
            nums[store_idx], nums[right] = nums[right], nums[store_idx]  # Move pivot to final position
            return store_idx

        # Step 1: Find Median (QuickSelect O(n))
        n = len(nums)
        median = quickselect(n // 2)

        # Step 2: Virtual Index Mapping (Three-way Partitioning)
        def index_map(i: int):
            """ Virtual indexing: Map indices to ensure correct ordering. """
            return (2 * i + 1) % (n | 1)  # Ensures interleaving of large/small elements

        # Three-way Dutch Partitioning
        left, i, right = 0, 0, n - 1
        while i <= right:
            mapped_i = index_map(i)
            if nums[mapped_i] > median:  # Large numbers to the left
                nums[index_map(left)], nums[mapped_i] = nums[mapped_i], nums[index_map(left)]
                left += 1
                i += 1
            elif nums[mapped_i] < median:  # Small numbers to the right
                nums[index_map(right)], nums[mapped_i] = nums[mapped_i], nums[index_map(right)]
                right -= 1
            else:
                i += 1


# Problem 324
# Link: https://leetcode.com/problems/wiggle-sort-ii/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1, 5, 1, 1, 6, 4], [1,6,1,5,1,4]),
        ([1, 3, 2, 2, 3, 1], [2,3,1,3,1,2]),
    ]
    for nums, expected in cases:
        s.wiggleSort(nums)
        assert nums == expected
