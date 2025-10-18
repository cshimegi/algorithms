# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?

# COMPLEXITY ANALYSIS:
#
# Problem: Find maximum sum of two numbers with equal digit sum
# Key insight: Group numbers by their digit sum, then find max sum from each group
#
# Both implementations have the same core logic but different data structures:
# - Implementation 1: Uses array of lists (pre-allocated)
# - Implementation 2: Uses dictionary with tuple tracking (space-efficient)
#
# DETAILED COMPLEXITY BREAKDOWN:
#
# COMMON OPERATIONS (both implementations):
# - Digit sum calculation: O(log(n)) per number
# - Total for n numbers: O(n * log(max_num))
#
# IMPLEMENTATION 1 DIFFERENCES:
# - Space: O(82 + n) - pre-allocates array of 82 lists + stores all numbers
# - Time: O(n * log(max_num) + k * m * log(m))
#   * k = number of non-empty groups (≤ 82)
#   * m = average group size
#   * Sorting each group: O(m * log(m))
#
# IMPLEMENTATION 2 DIFFERENCES:
# - Space: O(k) where k = unique digit sums (≤ 82)
# - Time: O(n * log(max_num)) - no sorting needed!
#   * Only tracks top 2 numbers per group
#   * Constant time updates: O(1)
#
# WINNER: Implementation 2 is significantly more efficient!
from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # IMPLEMENTATION 1: Array of lists approach
        # Time: O(n * log(max_num) + k * m * log(m)) where k = number of groups, m = avg group size
        # Space: O(9*9+1 + n) = O(82 + n) = O(n)
        
        records = [[] for _ in range(9*9+1)] # n <= 10^9 so max sum of digits is 999999999
        for n in nums:
            # Compute digit sum: O(log(n)) time
            digits_sum = 0
            temp = n
            while temp > 0:
                digits_sum += temp % 10
                temp //= 10
            records[digits_sum].append(n)  # O(1) append

        ans = -1
        for record in records:  # Iterate through 82 possible digit sums
            if len(record) >= 2:
                # Sort and take top 2: O(m * log(m)) where m = len(record)
                ans = max(ans, sum(sorted(record, reverse=True)[:2]))

        return ans

    def maximumSum2(self, nums: List[int]) -> int:
        # IMPLEMENTATION 2: Dictionary with tuple tracking approach
        # Time: O(n * log(max_num)) - much more efficient!
        # Space: O(k) where k = number of unique digit sums (at most 82)
        
        records = {}  # Dictionary to store max two values per digit sum
        ans = -1

        for n in nums:
            # Compute digit sum: O(log(n)) time
            digits_sum = 0
            temp = n
            while temp > 0:
                digits_sum += temp % 10
                temp //= 10

            # Track top 2 largest numbers for each sum of digits: O(1) operations
            if digits_sum in records:
                # If there's already a max value, update second max
                first, second = records[digits_sum][0], n
                if first < second:
                    first, second = second, first
                records[digits_sum] = (first, second)
                ans = max(ans, first + second)  # Update answer: O(1)
            else:
                # First number in the bucket
                records[digits_sum] = (n, -1)

        return ans

# Problem 2342
# Link: https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([18,43,36,13,7], 54),
        ([10,12,19,14], -1),
    ]
    for nums, expected in cases:
        assert s.maximumSum(nums) == expected
