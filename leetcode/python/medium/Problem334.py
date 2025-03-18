# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(1)
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')  # Smallest value
        second = float('inf')  # Second smallest value

        for num in nums:
            if num <= first:
                first = num  # Update smallest number
            elif num <= second:
                second = num  # Update second smallest number
            else:
                return True  # Found a third number > second

        return False

    def increasingTriplet2(self, nums: List[int]) -> List[int] | None:
        """
        Return triplet indices
        :param nums:
        :return:
        """
        first = float('inf')  # Smallest value
        first_idx = -1
        second = float('inf')  # Second smallest value
        second_idx = -1

        for idx, num in enumerate(nums):
            if num <= first:
                first = num  # Update smallest number
                first_idx = idx
            elif num <= second:
                second = num  # Update second smallest number
                second_idx = idx
            else:
                return [first_idx, second_idx, idx]

        return None


# Problem 334
# Link: https://leetcode.com/problems/increasing-triplet-subsequence/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1,2,3,4,5], True),
        ([5,4,3,2,1], False),
        ([2,1,5,0,4,6], True),
    ]
    for nums, expected in cases:
        assert s.increasingTriplet(nums) == expected
