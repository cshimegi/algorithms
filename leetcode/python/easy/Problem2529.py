# Questions to ask:
# 1. What is the time complexity? O(log(n))
# 2. What is the space complexity? O(1)
from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def binarySearch(find_negative: bool) -> int:
            left, right = 0, total
            while left < right:
                mid = (left+right)//2
                if find_negative:
                    if nums[mid] < 0:
                        left = mid+1
                    else:
                        right = mid
                else:
                    if nums[mid] > 0:
                        right = mid
                    else:
                        left = mid+1
            return left


        total = len(nums)
        maxNegativeIdx = binarySearch(True)
        minPositiveIdx = binarySearch(False)

        return max(maxNegativeIdx+1, total-minPositiveIdx)


# Problem 2529
# Tips:
# Link: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        [-2, -1, -1, 1, 2, 3],
        [-3, -2, -1, 0, 0, 1, 2],
        [5, 20, 66, 1314],
    ]
    for case in cases:
        print(s.maximumCount(case))

