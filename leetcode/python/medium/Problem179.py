# Questions to ask:
# 1. What is the time complexity? O(n*log(n))
# 2. What is the space complexity? O(n)
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        # Sort using a lambda function to define the key
        # Choosing 10 is because nums[i] <= 10^9
        nums.sort(key=lambda x: x*10, reverse=True)
        # Join the numbers to form the largest number
        ans = ''.join(nums)
        # Handle the case where the ans is all zeros
        return "0" if ans[0] == "0" else ans


# Problem 179
# Link: https://leetcode.com/problems/largest-number/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([10, 2], "210"),
        ([3, 30, 34, 5, 9], "9534330")
    ]
    for nums, expected in cases:
        assert s.largestNumber(nums) == expected
