# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(n)
from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller, equal, greater = [], [], []
        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        return smaller + equal + greater


# Problem 2161
# Link: https://leetcode.com/problems/partition-array-according-to-given-pivot/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([9,12,5,10,14,3,10], 10, [9, 5, 3, 10, 10, 12, 14]),
        ([2,3,5,8,4], 3, [2, 3, 5, 8, 4]),
    ]
    for nums, pivot, expected in cases:
        assert s.pivotArray(nums, pivot) == expected
