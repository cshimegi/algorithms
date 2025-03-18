# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        records = [[] for _ in range(9*9+1)] # n <= 10^9 so max sum of digits is 999999999
        for n in nums:
            digits_sum = 0
            temp = n
            while temp > 0:
                digits_sum += temp % 10
                temp //= 10
            records[digits_sum].append(n)

        ans = -1
        for record in records:
            if len(record) >= 2:
                ans = max(ans, sum(sorted(record, reverse=True)[:2]))

        return ans

    def maximumSum2(self, nums: List[int]) -> int:
        records = {}  # Dictionary to store max two values per digit sum
        ans = -1

        for n in nums:
            # Compute digit sum
            digits_sum = 0
            temp = n
            while temp > 0:
                digits_sum += temp % 10
                temp //= 10

            # Track top 2 largest numbers for each sum of digits
            if digits_sum in records:
                # If there's already a max value, update second max
                first, second = records[digits_sum][0], n
                if first < second:
                    first, second = second, first
                records[digits_sum] = (first, second)
                ans = max(ans, first + second)  # Update answer
            else:
                # First number in the bucket
                records[digits_sum] = (n, -1)

        return ans

# Problem 2342
# Link: https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([18,43,36,13,7], 64),
        ([10,12,19,14], -1),
    ]
    for nums, expected in cases:
        assert s.maximumSum(nums) == expected
