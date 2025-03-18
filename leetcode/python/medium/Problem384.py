# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
from typing import List
import random

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.origin = nums[:]
        self.n = len(self.nums)

    def reset(self) -> List[int]:
        return self.origin

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums


# Problem 384
# Link: https://leetcode.com/problems/shuffle-an-array/description/
# Tips:
if __name__ == '__main__':
    s = Solution([1,2,3,4])

