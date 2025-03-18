# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(1)
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        ans = nums[0]
        curr = nums[0]
        for n in nums[1:]:
            curr = max(n, curr + n)
            ans = max(ans, curr)
        return ans

    def maxSubArray2(self, nums: List[int]) -> List[int]:
        # Advanced: Kadane's Algorithm to return that subarray
        ans = nums[0]
        curr = nums[0]
        start, end = 0, 0
        for idx, n in enumerate(nums[1:], start=1): # Start indexing at 1
            if n > curr + n:
                curr = n
                start = idx
            else:
                curr += n

            if curr > ans:
                ans = curr
                end = idx
        return nums[start:end+1]


# Problem 53
# Link: https://leetcode.com/problems/maximum-subarray/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),
        ([1], 1),
        ([5,4,-1,7,8], 23),
        ([1, -2, 3, -1, 2, -1, 2, -5, 4], 5)
    ]

    for nums, expected in cases:
        assert s.maxSubArray(nums) == expected
        print(s.maxSubArray2(nums))
