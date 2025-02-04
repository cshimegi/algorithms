# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.origin = nums[:]
        self.n = len(self.nums)

    def reset(self) -> list[int]:
        return self.origin

    def shuffle(self) -> list[int]:
        random.shuffle(self.nums)
        return self.nums


# Problem 384
# Link: https://leetcode.com/problems/shuffle-an-array/description/
# Tips:
if __name__ == '__main__':
    s = Solution([1,2,3,4])

